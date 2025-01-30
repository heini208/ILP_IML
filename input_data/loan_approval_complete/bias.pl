head_pred(loan_approved, 1).
body_pred(person_age, 2).
body_pred(person_gender, 2).
body_pred(person_education, 2).
body_pred(person_income, 2).
body_pred(person_emp_exp, 2).
body_pred(person_home_ownership, 2).
body_pred(loan_amnt, 2).
body_pred(loan_intent, 2).
body_pred(loan_int_rate, 2).
body_pred(loan_percent_income, 2).
body_pred(cb_person_cred_hist_length, 2).
body_pred(credit_score, 2).
body_pred(previous_loan_defaults_on_file, 2).

type(loan_approved, (person,)).
type(person_age, (person, int)).
type(person_gender, (person, gender)).
type(person_education, (person, education)).
type(person_income, (person, int)).
type(person_emp_exp, (person, int)).
type(person_home_ownership, (person, home_ownership)).
type(loan_amnt, (person, int)).
type(loan_intent, (person, intent)).
type(loan_int_rate, (person, float)).
type(loan_percent_income, (person, float)).
type(cb_person_cred_hist_length, (person, int)).
type(credit_score, (person, int)).
type(previous_loan_defaults_on_file, (person, bool)).

% bk.pl
person_age(p1, 22).
person_gender(p1, female).
person_education(p1, master).
person_income(p1, 71948).
person_emp_exp(p1, 0).
person_home_ownership(p1, rent).
loan_amnt(p1, 35000).
loan_intent(p1, personal).
loan_int_rate(p1, 16.02).
loan_percent_income(p1, 0.49).
cb_person_cred_hist_length(p1, 3).
credit_score(p1, 561).
previous_loan_defaults_on_file(p1, no).

person_age(p2, 21).
person_gender(p2, female).
person_education(p2, high_school).
person_income(p2, 12282).
person_emp_exp(p2, 0).
person_home_ownership(p2, own).
loan_amnt(p2, 1000).
loan_intent(p2, education).
loan_int_rate(p2, 11.14).
loan_percent_income(p2, 0.08).
cb_person_cred_hist_length(p2, 2).
credit_score(p2, 504).
previous_loan_defaults_on_file(p2, yes).