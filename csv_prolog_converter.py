import os
import json
import pandas as pd

with open("settings.json", "r") as f:
    settings = json.load(f)

data_settings_path = settings.get("data_settings_path", "data_settings.json")
with open(data_settings_path, "r") as f:
    data_settings = json.load(f)

experiment_name = settings["experiment_name"]
data_limit = min(max(settings.get("data_limit", 40000), 1), 40000)

classification_column = data_settings["classification_column"]
classification_target = data_settings["classification_target"]
classification_target_value = data_settings.get("classification_target_value", 1)

categories = {k: v for k, v in data_settings["categories"].items() if not v.get("exclude", False)}
binary_categories = {k: v for k, v in data_settings["binary_categories"].items() if not v.get("exclude", False)}
categorical_mappings = {k: v for k, v in data_settings["categorical_mappings"].items() if not v.get("exclude", False)}
feature_interactions = data_settings.get("feature_interactions", {})

input_data_dir = os.path.join("input_data", experiment_name)
os.makedirs(input_data_dir, exist_ok=True)

csv_file_path = data_settings["csv_file_path"]
bk_loan_path = os.path.join(input_data_dir, "bk.pl")
exs_loan_path = os.path.join(input_data_dir, "exs.pl")
bias_loan_path = os.path.join(input_data_dir, "bias.pl")

df = pd.read_csv(csv_file_path).head(data_limit)

def evaluate_condition(row, condition):
    feature, operator, value = condition["feature"], condition["operator"], condition["value"]
    if isinstance(value, str):
        value = f'"{value}"'
    return eval(f'row["{feature}"] {operator} {value}')

for feature_name, interaction in feature_interactions.items():
    df[feature_name] = df.apply(lambda row: all(evaluate_condition(row, cond) for cond in interaction["conditions"]), axis=1)

predicates = ["applicant"]
for category in categories.values():
    predicates.extend(category["labels"])
for category in categorical_mappings.values():
    predicates.extend(category["mapping"].values())
for category in binary_categories.values():
    predicates.extend(category["labels"])
for feature_name in feature_interactions.keys():
    predicates.append(feature_name)

bk_facts = {pred: [] for pred in predicates}
exs_pos_entries = []
exs_neg_entries = []

for index, row in df.iterrows():
    applicant_id = f"p{index}"
    bk_facts["applicant"].append(f"applicant({applicant_id}).")

    for column, config in categories.items():
        labels, thresholds = config["labels"], config["thresholds"]
        for i, threshold in enumerate(thresholds):
            if row[column] < threshold:
                bk_facts[labels[i]].append(f"{labels[i]}({applicant_id}).")
                break
        else:
            bk_facts[labels[-1]].append(f"{labels[-1]}({applicant_id}).")

    for column, config in categorical_mappings.items():
        mapping = config["mapping"]
        value = mapping.get(str(row[column]))
        if value:
            bk_facts[value].append(f"{value}({applicant_id}).")

    for column, config in binary_categories.items():
        labels, values = config["labels"], config["values"]
        label = labels[values.index(str(row[column]))] if str(row[column]) in values else None
        if label:
            bk_facts[label].append(f"{label}({applicant_id}).")

    for feature_name in feature_interactions.keys():
        if row[feature_name]:
            bk_facts[feature_name].append(f"{feature_name}({applicant_id}).")

    if row[classification_column] == classification_target_value:
        exs_pos_entries.append(f"pos({classification_target}({applicant_id})).")
    else:
        exs_neg_entries.append(f"neg({classification_target}({applicant_id})).")

with open(bk_loan_path, "w") as bk_file:
    for category, facts in bk_facts.items():
        bk_file.write(f"% {category}\n")
        bk_file.write("\n".join(facts))
        bk_file.write("\n\n")

with open(exs_loan_path, "w") as exs_file:
    exs_file.write("% Positive Examples\n" + "\n".join(exs_pos_entries) + "\n\n")
    exs_file.write("% Negative Examples\n" + "\n".join(exs_neg_entries))

with open(bias_loan_path, "w") as bias_file:
    if "max_vars" in settings["popper_settings"]:
        bias_file.write(f"max_vars({settings['popper_settings']['max_vars']}).\n")
    if "max_body" in settings["popper_settings"]:
        bias_file.write(f"max_body({settings['popper_settings']['max_body']}).\n")
    
    bias_file.write(f"\nhead_pred({classification_target},1).\n\n")

    for pred in predicates:
        if pred != "applicant":
            bias_file.write(f"body_pred({pred},1).\n")

    bias_file.write("\n% Direction of predicates\n")
    bias_file.write(f"direction({classification_target},(in,)).\n")
    for pred in predicates:
        bias_file.write(f"direction({pred},(in,)).\n")

    bias_file.write("\n% Type definitions\n")
    bias_file.write(f"type({classification_target},(applicant,)).\n")
    for pred in predicates:
        bias_file.write(f"type({pred},(applicant,)).\n")

print(f"Prolog files saved in: {input_data_dir}\nGenerated: bk.pl, exs.pl, bias.pl")
