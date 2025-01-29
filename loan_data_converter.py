import pandas as pd
import random

# File paths
loan_file_path = "loan_data.csv"  # Update with actual path
bk_loan_path = "bk.pl"
exs_loan_path = "exs.pl"

# Load dataset
df = pd.read_csv(loan_file_path)

# List of predicates to generate
predicates = [
    "person_income", "loan_amnt", "loan_int_rate", "loan_percent_income",
    "high_income", "low_income", "high_credit", "low_credit",
    "high_interest", "low_interest", "has_default", "no_default", "applicant"
]

# Initialize storage for facts
bk_facts = {pred: [] for pred in predicates}

# Storage for positive and negative examples
exs_pos_entries = []
exs_neg_entries = []

# Sample size to reduce dataset for efficiency
sample_size = 10000  # Adjust as needed
sampled_df = df.sample(n=sample_size, random_state=42)

for index, row in sampled_df.iterrows():
    applicant_id = f"p{index}"

    bk_facts["applicant"].append(f"applicant({applicant_id}).")

    # Numerical attributes
    income_value = row["person_income"]
    loan_amnt_value = row["loan_amnt"]
    int_rate_value = row["loan_int_rate"]
    percent_income_value = row["loan_percent_income"]

    bk_facts["person_income"].append(f"person_income({applicant_id}, {income_value:.2f}).")
    bk_facts["loan_amnt"].append(f"loan_amnt({applicant_id}, {loan_amnt_value:.2f}).")
    bk_facts["loan_int_rate"].append(f"loan_int_rate({applicant_id}, {int_rate_value:.2f}).")
    bk_facts["loan_percent_income"].append(f"loan_percent_income({applicant_id}, {percent_income_value:.2f}).")

    # Derived categorical predicates
    if income_value > 50000:
        bk_facts["high_income"].append(f"high_income({applicant_id}).")
    else:
        bk_facts["low_income"].append(f"low_income({applicant_id}).")

    credit_score_value = row["credit_score"]
    if credit_score_value > 650:
        bk_facts["high_credit"].append(f"high_credit({applicant_id}).")
    else:
        bk_facts["low_credit"].append(f"low_credit({applicant_id}).")

    if int_rate_value > 12.0:
        bk_facts["high_interest"].append(f"high_interest({applicant_id}).")
    else:
        bk_facts["low_interest"].append(f"low_interest({applicant_id}).")

    # Previous loan defaults
    if row["previous_loan_defaults_on_file"] == "Yes":
        bk_facts["has_default"].append(f"has_default({applicant_id}).")
    else:
        bk_facts["no_default"].append(f"no_default({applicant_id}).")

    # Loan approval classification examples
    if row["loan_status"] == 1:
        exs_pos_entries.append(f"pos(approved({applicant_id})).")
    else:
        exs_neg_entries.append(f"neg(approved({applicant_id})).")

# Write `bk.pl`
with open(bk_loan_path, "w") as bk_file:
    bk_file.write(":- style_check(-discontiguous).\n\n")
    for pred in predicates:
        bk_file.write(f":- discontiguous {pred}/1.\n")
    bk_file.write("\n")

    for category, facts in bk_facts.items():
        bk_file.write(f"% {category}\n") 
        bk_file.write("\n".join(sorted(facts)))
        bk_file.write("\n\n")

# Write `exs.pl`
with open(exs_loan_path, "w") as exs_file:
    exs_file.write("% Positive Examples\n")
    exs_file.write("\n".join(exs_pos_entries))
    exs_file.write("\n\n% Negative Examples\n")
    exs_file.write("\n".join(exs_neg_entries))

print("Prolog files generated: bk.pl, exs.pl")
