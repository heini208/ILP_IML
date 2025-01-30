import os
import json
import pandas as pd

# Load settings.json
with open("settings.json", "r") as f:
    settings = json.load(f)

experiment_name = settings["experiment_name"]
data_limit = min(max(settings.get("data_limit", 40000), 1), 40000)
categories = {k: v for k, v in settings["categories"].items() if not v.get("exclude", False)}
binary_categories = {k: v for k, v in settings["binary_categories"].items() if not v.get("exclude", False)}
categorical_mappings = {k: v for k, v in settings["categorical_mappings"].items() if not v.get("exclude", False)}
feature_interactions = settings.get("feature_interactions", {})
popper_settings = settings["popper_settings"]

# Create input data directory
input_data_dir = os.path.join("input_data", experiment_name)
os.makedirs(input_data_dir, exist_ok=True)

# Define file paths
loan_file_path = "loan_data.csv"
bk_loan_path = os.path.join(input_data_dir, "bk.pl")
exs_loan_path = os.path.join(input_data_dir, "exs.pl")
bias_loan_path = os.path.join(input_data_dir, "bias.pl")

# Load the dataset
df = pd.read_csv(loan_file_path).head(data_limit)

# Generate feature interaction columns
def evaluate_condition(row, condition):
    """Evaluates a single condition for a feature interaction."""
    feature, operator, value = condition["feature"], condition["operator"], condition["value"]
    if operator == "<":
        return row[feature] < value
    elif operator == ">":
        return row[feature] > value
    elif operator == "<=":
        return row[feature] <= value
    elif operator == ">=":
        return row[feature] >= value
    elif operator == "==":
        return row[feature] == value
    elif operator == "!=":
        return row[feature] != value
    else:
        raise ValueError(f"Unsupported operator: {operator}")

# Apply feature interactions
for feature_name, interaction in feature_interactions.items():
    conditions = interaction["conditions"]
    df[feature_name] = df.apply(lambda row: all(evaluate_condition(row, cond) for cond in conditions), axis=1)

# Initialize predicates
predicates = ["applicant"]
for category in categories.values():
    predicates.extend(category["labels"])
for category in categorical_mappings.values():
    predicates.extend(category["mapping"].values())
for category in binary_categories.values():
    predicates.extend(category["labels"])
for feature_name in feature_interactions.keys():
    predicates.append(feature_name)

# Initialize data structures
bk_facts = {pred: [] for pred in predicates}
exs_pos_entries = []
exs_neg_entries = []

# Process dataset rows
for index, row in df.iterrows():
    applicant_id = f"p{index}"
    bk_facts["applicant"].append(f"applicant({applicant_id}).")

    # Process categorical variables
    for column, config in categories.items():
        labels, thresholds = config["labels"], config["thresholds"]
        for i, threshold in enumerate(thresholds):
            if row[column] < threshold:
                bk_facts[labels[i]].append(f"{labels[i]}({applicant_id}).")
                break
        else:
            bk_facts[labels[-1]].append(f"{labels[-1]}({applicant_id}).")

    # Fix: Correctly retrieve mapping before accessing values
    for column, config in categorical_mappings.items():
        mapping = config["mapping"]  # Retrieve mapping dictionary
        value = mapping.get(row[column])  # Safely get mapped value
        if value:
            bk_facts[value].append(f"{value}({applicant_id}).")

    for column, config in binary_categories.items():
        labels, values = config["labels"], config["values"]
        label = labels[values.index(row[column])] if row[column] in values else None
        if label:
            bk_facts[label].append(f"{label}({applicant_id}).")

    # Process feature interactions
    for feature_name in feature_interactions.keys():
        if row[feature_name]:
            bk_facts[feature_name].append(f"{feature_name}({applicant_id}).")

    # Process loan status examples
    if row["loan_status"] == 1:
        exs_pos_entries.append(f"pos(approved({applicant_id})).")
    else:
        exs_neg_entries.append(f"neg(approved({applicant_id})).")

# Write `bk.pl` file
with open(bk_loan_path, "w") as bk_file:
    for category, facts in bk_facts.items():
        bk_file.write(f"% {category}\n")
        bk_file.write("\n".join(facts))
        bk_file.write("\n\n")

# Write `exs.pl` file
with open(exs_loan_path, "w") as exs_file:
    exs_file.write("% Positive Examples\n")
    exs_file.write("\n".join(exs_pos_entries))
    exs_file.write("\n\n% Negative Examples\n")
    exs_file.write("\n".join(exs_neg_entries))

# Write `bias.pl` file
with open(bias_loan_path, "w") as bias_file:
    if "max_vars" in popper_settings:
        bias_file.write(f"max_vars({popper_settings['max_vars']}).\n")
    if "max_body" in popper_settings:
        bias_file.write(f"max_body({popper_settings['max_body']}).\n")
    bias_file.write("\n")

    bias_file.write("head_pred(approved,1).\n\n")

    for pred in predicates:
        if pred != "applicant":
            bias_file.write(f"body_pred({pred},1).\n")

    bias_file.write("\n% Type Definitions\n")
    bias_file.write("type(approved, (person,)).\n")

    for pred in predicates:
        if pred != "applicant":
            bias_file.write(f"type({pred}, (person,)).\n")

    bias_file.write("\n% Directions\n")
    bias_file.write("direction(approved, (in,)).\n")

    for pred in predicates:
        if pred != "applicant":
            bias_file.write(f"direction({pred}, (in,)).\n")

print(f"Prolog files saved in: {input_data_dir}\nGenerated: bk.pl, exs.pl, bias.pl")
