max_rules(5).
max_literals(5).
max_body(6).
max_vars(6).

head_pred(approved,1).

body_pred(person_income,2).
body_pred(loan_amnt,2).
body_pred(loan_int_rate,2).
body_pred(loan_percent_income,2).
body_pred(high_income,1).
body_pred(low_income,1).
body_pred(high_credit,1).
body_pred(low_credit,1).
body_pred(has_default,1).
body_pred(no_default,1).
body_pred(high_interest,1).
body_pred(low_interest,1).

type(approved, (person,)).
type(person_income, (person, real)).
type(loan_amnt, (person, real)).
type(loan_int_rate, (person, real)).
type(loan_percent_income, (person, real)).
type(high_income, (person,)).
type(low_income, (person,)).
type(high_credit, (person,)).
type(low_credit, (person,)).
type(has_default, (person,)).
type(no_default, (person,)).
type(high_interest, (person,)).
type(low_interest, (person,)).

direction(approved, (in,)).
direction(person_income, (in, out)).
direction(loan_amnt, (in, out)).
direction(loan_int_rate, (in, out)).
direction(loan_percent_income, (in, out)).
direction(high_income, (in,)).
direction(low_income, (in,)).
direction(high_credit, (in,)).
direction(low_credit, (in,)).
direction(has_default, (in,)).
direction(no_default, (in,)).
direction(high_interest, (in,)).
direction(low_interest, (in,)).

enable_pi.
