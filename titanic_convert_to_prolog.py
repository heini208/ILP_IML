import pandas as pd

# File paths
file_path = "titanic_data.csv"  # Adjust if necessary
df = pd.read_csv(file_path)

bk_path = "bk.pl"
exs_path = "exs.pl"

# Define predicates based on Titanic dataset attributes (with correct capitalization)
predicates = [
    "pclass", "sex_male", "sex_female", "age", "sibsp", "parch", "fare", 
    "embarked_c", "embarked_s", "embarked_q", "passenger", 
    "child", "adult", "elderly", "low_fare", "high_fare"  # New derived predicates
]

# Initialize dictionary for storing facts
bk_facts = {pred: [] for pred in predicates}

# Lists to store positive and negative examples
exs_pos_entries = []
exs_neg_entries = []

for _, row in df.iterrows():
    passenger_id = f"p{int(row['PassengerId'])}"  # Use actual PassengerId

    bk_facts["passenger"].append(f"passenger({passenger_id}).")

    for col in df.columns:
        if col in ["PassengerId", "Survived", "Name", "Ticket", "Cabin"]:
            continue  # Skip PassengerId (used already), Survived (goes in exs.pl), and text-heavy fields

        value = row[col]

        if col == "Sex":
            if value == "male":
                bk_facts["sex_male"].append(f"sex_male({passenger_id}).")
            elif value == "female":
                bk_facts["sex_female"].append(f"sex_female({passenger_id}).")
            continue  # Skip further processing for `Sex`, already handled

        if col == "Embarked":
            if value == "C":
                bk_facts["embarked_c"].append(f"embarked_c({passenger_id}).")
            elif value == "Q":
                bk_facts["embarked_q"].append(f"embarked_q({passenger_id}).")
            elif value == "S":
                bk_facts["embarked_s"].append(f"embarked_s({passenger_id}).")
            continue  # Skip further processing

        elif pd.isna(value):
            continue  # Skip missing values

        else:
            value = f"{value:.2f}"  # Format numerical values

        # Convert column names to lowercase Prolog predicates
        predicate = col.lower()
        bk_facts[predicate].append(f"{predicate}({passenger_id}, {value}).")

    # Add age category predicates
    if "Age" in row and not pd.isna(row["Age"]):
        age_value = row["Age"]
        if age_value < 18:
            bk_facts["child"].append(f"child({passenger_id}).")
        elif age_value >= 65:
            bk_facts["elderly"].append(f"elderly({passenger_id}).")
        else:
            bk_facts["adult"].append(f"adult({passenger_id}).")

    # Add fare category predicates
    if "Fare" in row and not pd.isna(row["Fare"]):
        fare_value = row["Fare"]
        if fare_value > 50:
            bk_facts["high_fare"].append(f"high_fare({passenger_id}).")
        else:
            bk_facts["low_fare"].append(f"low_fare({passenger_id}).")

    # Add survival examples to exs.pl
    if row["Survived"] == 1:
        exs_pos_entries.append(f"pos(survived({passenger_id})).")
    else:
        exs_neg_entries.append(f"neg(survived({passenger_id})).")

# Write `bk.pl`
with open(bk_path, "w") as bk_file:
    bk_file.write(":- style_check(-discontiguous).\n\n")
    for pred in predicates:
        bk_file.write(f":- discontiguous {pred}/2.\n")
    bk_file.write("\n")

    for category, facts in bk_facts.items():
        if facts:  # Only write non-empty categories
            bk_file.write(f"% {category}\n")
            bk_file.write("\n".join(sorted(facts)))
            bk_file.write("\n\n")

# Write `exs.pl`
with open(exs_path, "w") as exs_file:
    exs_file.write("% Positive Examples\n")
    exs_file.write("\n".join(exs_pos_entries))
    exs_file.write("\n\n% Negative Examples\n")
    exs_file.write("\n".join(exs_neg_entries))

print("Prolog files generated: bk.pl, exs.pl")
