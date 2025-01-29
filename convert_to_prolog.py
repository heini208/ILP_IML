import pandas as pd
import random

file_path = "loan_data.csv"
df = pd.read_csv(file_path)

bk_path = "bk.pl"
exs_path = "exs.pl"

# List of predicates that need discontiguous declarations
predicates = [
    "person_age", "person_gender", "person_education", "person_income",
    "person_emp_exp", "person_home_ownership", "loan_amnt", "loan_intent",
    "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length",
    "credit_score", "previous_loan_defaults_on_file", "applicant"
]

bk_facts = {pred: [] for pred in predicates}

exs_pos_entries = []
exs_neg_entries = []

# Set the sample size (you can adjust this as needed)
sample_size = 5000  # Adjust the number based on how much data you want to use

# Randomly sample rows from the DataFrame
sampled_df = df.sample(n=sample_size, random_state=42)

for index, row in sampled_df.iterrows():
    applicant_id = f"p{index}"
    bk_facts["applicant"].append(f"applicant({applicant_id}).")

    for col in df.columns:
        if col in ["loan_status", "person_age", "loan_percent_income", "loan_int_rate", "person_emp_exp"]:
            continue  

        value = row[col]
        
        if col in ["person_gender", "person_education", "person_home_ownership", "loan_intent", "previous_loan_defaults_on_file"]:
            value = f"'{value}'"  # Enclose in single quotes
        
        elif isinstance(value, str):
            value = f"{value}"

        else:
            value = f"{value:.2f}"

        bk_facts[col].append(f"{col}({applicant_id}, {value}).")

    # Add examples to exs.pl
    if row["loan_status"] == 1:
        exs_pos_entries.append(f"pos(loan_approved({applicant_id})).")
    else:
        exs_neg_entries.append(f"neg(loan_approved({applicant_id})).")

with open(bk_path, "w") as bk_file:
    bk_file.write(":- style_check(-discontiguous).\n\n")
    for pred in predicates:
        bk_file.write(f":- discontiguous {pred}/2.\n")
    bk_file.write("\n")

    for category, facts in bk_facts.items():
        bk_file.write(f"% {category}\n") 
        bk_file.write("\n".join(sorted(facts)))
        bk_file.write("\n\n")

# Write `exs.pl`
with open(exs_path, "w") as exs_file:
    exs_file.write("\n".join(exs_pos_entries))
    exs_file.write("\n")
    exs_file.write("\n".join(exs_neg_entries))

print("Prolog files generated: bk.pl, exs.pl")
