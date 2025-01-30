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
    "very_young", "young", "middle_aged", "senior",  # More detailed Age categories
    "very_low_ratio", "low_ratio", "medium_ratio", "high_ratio", "very_high_ratio",  # More detailed Loan percent income categories
    "very_low_income", "low_income", "medium_income", "high_income",  # More detailed Income categories
    "subprime_credit", "poor_credit", "fair_credit", "good_credit", "excellent_credit",  # More detailed Credit Score categories
    "very_high_interest", "high_interest", "medium_high_interest", "medium_interest", "low_interest",  # More detailed Interest Rate categories
    "has_default", "no_default", "high_risk", "low_risk", "loan_shark", "applicant"
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
    age_value = row["person_age"]
    credit_score_value = row["credit_score"]

    bk_facts["person_income"].append(f"person_income({applicant_id}, {income_value:.2f}).")
    bk_facts["loan_amnt"].append(f"loan_amnt({applicant_id}, {loan_amnt_value:.2f}).")
    bk_facts["loan_int_rate"].append(f"loan_int_rate({applicant_id}, {int_rate_value:.2f}).")
    bk_facts["loan_percent_income"].append(f"loan_percent_income({applicant_id}, {percent_income_value:.2f}).")

    # More Detailed Age Levels
    if age_value < 25:
        bk_facts["very_young"].append(f"very_young({applicant_id}).")
    elif age_value < 35:
        bk_facts["young"].append(f"young({applicant_id}).")
    elif age_value < 60:
        bk_facts["middle_aged"].append(f"middle_aged({applicant_id}).")
    else:
        bk_facts["senior"].append(f"senior({applicant_id}).")

    # More Detailed Loan Percent Income
    if percent_income_value < 0.15:
        bk_facts["very_low_ratio"].append(f"very_low_ratio({applicant_id}).")
    elif percent_income_value < 0.25:
        bk_facts["low_ratio"].append(f"low_ratio({applicant_id}).")
    elif percent_income_value < 0.35:
        bk_facts["medium_ratio"].append(f"medium_ratio({applicant_id}).")
    elif percent_income_value < 0.45:
        bk_facts["high_ratio"].append(f"high_ratio({applicant_id}).")
    else:
        bk_facts["very_high_ratio"].append(f"very_high_ratio({applicant_id}).")

    # More Detailed Income Levels
    if income_value < 25000:
        bk_facts["very_low_income"].append(f"very_low_income({applicant_id}).")
    elif income_value < 50000:
        bk_facts["low_income"].append(f"low_income({applicant_id}).")
    elif income_value < 100000:
        bk_facts["medium_income"].append(f"medium_income({applicant_id}).")
    else:
        bk_facts["high_income"].append(f"high_income({applicant_id}).")

    # More Detailed Credit Score Levels
    if credit_score_value < 500:
        bk_facts["subprime_credit"].append(f"subprime_credit({applicant_id}).")
    elif credit_score_value < 600:
        bk_facts["poor_credit"].append(f"poor_credit({applicant_id}).")
    elif credit_score_value < 700:
        bk_facts["fair_credit"].append(f"fair_credit({applicant_id}).")
    elif credit_score_value < 750:
        bk_facts["good_credit"].append(f"good_credit({applicant_id}).")
    else:
        bk_facts["excellent_credit"].append(f"excellent_credit({applicant_id}).")

    # More Detailed Interest Rate Levels
    if int_rate_value > 20:
        bk_facts["very_high_interest"].append(f"very_high_interest({applicant_id}).")
    elif int_rate_value > 15:
        bk_facts["high_interest"].append(f"high_interest({applicant_id}).")
    elif int_rate_value > 10:
        bk_facts["medium_high_interest"].append(f"medium_high_interest({applicant_id}).")
    elif int_rate_value > 5:
        bk_facts["medium_interest"].append(f"medium_interest({applicant_id}).")
    else:
        bk_facts["low_interest"].append(f"low_interest({applicant_id}).")

    # Previous loan defaults
    if row["previous_loan_defaults_on_file"] == "Yes":
        bk_facts["has_default"].append(f"has_default({applicant_id}).")
    else:
        bk_facts["no_default"].append(f"no_default({applicant_id}).")

    # Feature Interactions (High-Risk, Low-Risk, Loan Shark)
    if income_value < 40000 and credit_score_value < 600:
        bk_facts["high_risk"].append(f"high_risk({applicant_id}).")

    if income_value > 80000 and credit_score_value > 750:
        bk_facts["low_risk"].append(f"low_risk({applicant_id}).")

    if int_rate_value > 15 and credit_score_value < 600:
        bk_facts["loan_shark"].append(f"loan_shark({applicant_id}).")

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
