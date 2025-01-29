max_rules(5).
max_literals(8).
max_body(10).
max_vars(10).

head_pred(approved,1).

body_pred(person_age,2).
body_pred(person_income,2).
body_pred(loan_amnt,2).
body_pred(loan_int_rate,2).
body_pred(loan_percent_income,2).
body_pred(credit_score,2).
body_pred(cb_person_cred_hist_length,2).
body_pred(person_gender_male,1).
body_pred(person_gender_female,1).
body_pred(person_education_high_school,1).
body_pred(person_education_bachelor,1).
body_pred(person_education_master,1).
body_pred(person_home_own,1).
body_pred(person_home_rent,1).
body_pred(person_home_mortgage,1).
body_pred(loan_intent_education,1).
body_pred(loan_intent_medical,1).
body_pred(loan_intent_personal,1).
body_pred(loan_intent_home_improvement,1).
body_pred(loan_intent_debt_consolidation,1).
body_pred(loan_intent_vehicle,1).
body_pred(has_default,1).
body_pred(no_default,1).
body_pred(high_income,1).
body_pred(low_income,1).
body_pred(high_credit,1).
body_pred(low_credit,1).
body_pred(high_interest,1).
body_pred(low_interest,1).
body_pred(child,1).
body_pred(adult,1).
body_pred(elderly,1).

type(approved, (person,)).
type(person_age, (person, real)).
type(person_income, (person, real)).
type(loan_amnt, (person, real)).
type(loan_int_rate, (person, real)).
type(loan_percent_income, (person, real)).
type(credit_score, (person, real)).
type(cb_person_cred_hist_length, (person, real)).
type(person_gender_male, (person,)).
type(person_gender_female, (person,)).
type(person_education_high_school, (person,)).
type(person_education_bachelor, (person,)).
type(person_education_master, (person,)).
type(person_home_own, (person,)).
type(person_home_rent, (person,)).
type(person_home_mortgage, (person,)).
type(loan_intent_education, (person,)).
type(loan_intent_medical, (person,)).
type(loan_intent_personal, (person,)).
type(loan_intent_home_improvement, (person,)).
type(loan_intent_debt_consolidation, (person,)).
type(loan_intent_vehicle, (person,)).
type(has_default, (person,)).
type(no_default, (person,)).
type(high_income, (person,)).
type(low_income, (person,)).
type(high_credit, (person,)).
type(low_credit, (person,)).
type(high_interest, (person,)).
type(low_interest, (person,)).
type(child, (person,)).
type(adult, (person,)).
type(elderly, (person,)).

direction(approved, (in,)).
direction(person_age, (in, out)).
direction(person_income, (in, out)).
direction(loan_amnt, (in, out)).
direction(loan_int_rate, (in, out)).
direction(loan_percent_income, (in, out)).
direction(credit_score, (in, out)).
direction(cb_person_cred_hist_length, (in, out)).
direction(person_gender_male, (in,)).
direction(person_gender_female, (in,)).
direction(person_education_high_school, (in,)).
direction(person_education_bachelor, (in,)).
direction(person_education_master, (in,)).
direction(person_home_own, (in,)).
direction(person_home_rent, (in,)).
direction(person_home_mortgage, (in,)).
direction(loan_intent_education, (in,)).
direction(loan_intent_medical, (in,)).
direction(loan_intent_personal, (in,)).
direction(loan_intent_home_improvement, (in,)).
direction(loan_intent_debt_consolidation, (in,)).
direction(loan_intent_vehicle, (in,)).
direction(has_default, (in,)).
direction(no_default, (in,)).
direction(high_income, (in,)).
direction(low_income, (in,)).
direction(high_credit, (in,)).
direction(low_credit, (in,)).
direction(high_interest, (in,)).
direction(low_interest, (in,)).
direction(child, (in,)).
direction(adult, (in,)).
direction(elderly, (in,)).

