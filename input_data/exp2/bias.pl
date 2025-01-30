max_vars(8).
max_body(8).

head_pred(approved,1).

body_pred(very_young,1).
body_pred(young,1).
body_pred(middle_aged,1).
body_pred(senior,1).
body_pred(very_low_income,1).
body_pred(low_income,1).
body_pred(medium_income,1).
body_pred(high_income,1).
body_pred(subprime_credit,1).
body_pred(poor_credit,1).
body_pred(fair_credit,1).
body_pred(good_credit,1).
body_pred(excellent_credit,1).
body_pred(very_small_loan,1).
body_pred(small_loan,1).
body_pred(medium_loan,1).
body_pred(large_loan,1).
body_pred(very_large_loan,1).
body_pred(very_low_ratio,1).
body_pred(low_ratio,1).
body_pred(medium_ratio,1).
body_pred(high_ratio,1).
body_pred(very_high_ratio,1).
body_pred(very_high_interest,1).
body_pred(high_interest,1).
body_pred(medium_high_interest,1).
body_pred(medium_interest,1).
body_pred(low_interest,1).
body_pred(short_history,1).
body_pred(medium_history,1).
body_pred(long_history,1).
body_pred(junior_experience,1).
body_pred(mid_experience,1).
body_pred(senior_experience,1).
body_pred(high_school,1).
body_pred(associate_degree,1).
body_pred(bachelor_degree,1).
body_pred(master_degree,1).
body_pred(doctorate,1).
body_pred(debt_consolidation,1).
body_pred(education_loan,1).
body_pred(medical_loan,1).
body_pred(personal_loan,1).
body_pred(venture_capital,1).
body_pred(home_improvement,1).
body_pred(male,1).
body_pred(female,1).
body_pred(has_default,1).
body_pred(no_default,1).
body_pred(renter,1).
body_pred(owner,1).
body_pred(high_risk,1).
body_pred(low_risk,1).

% Type Definitions
type(approved, (person,)).
type(very_young, (person,)).
type(young, (person,)).
type(middle_aged, (person,)).
type(senior, (person,)).
type(very_low_income, (person,)).
type(low_income, (person,)).
type(medium_income, (person,)).
type(high_income, (person,)).
type(subprime_credit, (person,)).
type(poor_credit, (person,)).
type(fair_credit, (person,)).
type(good_credit, (person,)).
type(excellent_credit, (person,)).
type(very_small_loan, (person,)).
type(small_loan, (person,)).
type(medium_loan, (person,)).
type(large_loan, (person,)).
type(very_large_loan, (person,)).
type(very_low_ratio, (person,)).
type(low_ratio, (person,)).
type(medium_ratio, (person,)).
type(high_ratio, (person,)).
type(very_high_ratio, (person,)).
type(very_high_interest, (person,)).
type(high_interest, (person,)).
type(medium_high_interest, (person,)).
type(medium_interest, (person,)).
type(low_interest, (person,)).
type(short_history, (person,)).
type(medium_history, (person,)).
type(long_history, (person,)).
type(junior_experience, (person,)).
type(mid_experience, (person,)).
type(senior_experience, (person,)).
type(high_school, (person,)).
type(associate_degree, (person,)).
type(bachelor_degree, (person,)).
type(master_degree, (person,)).
type(doctorate, (person,)).
type(debt_consolidation, (person,)).
type(education_loan, (person,)).
type(medical_loan, (person,)).
type(personal_loan, (person,)).
type(venture_capital, (person,)).
type(home_improvement, (person,)).
type(male, (person,)).
type(female, (person,)).
type(has_default, (person,)).
type(no_default, (person,)).
type(renter, (person,)).
type(owner, (person,)).
type(high_risk, (person,)).
type(low_risk, (person,)).

% Directions
direction(approved, (in,)).
direction(very_young, (in,)).
direction(young, (in,)).
direction(middle_aged, (in,)).
direction(senior, (in,)).
direction(very_low_income, (in,)).
direction(low_income, (in,)).
direction(medium_income, (in,)).
direction(high_income, (in,)).
direction(subprime_credit, (in,)).
direction(poor_credit, (in,)).
direction(fair_credit, (in,)).
direction(good_credit, (in,)).
direction(excellent_credit, (in,)).
direction(very_small_loan, (in,)).
direction(small_loan, (in,)).
direction(medium_loan, (in,)).
direction(large_loan, (in,)).
direction(very_large_loan, (in,)).
direction(very_low_ratio, (in,)).
direction(low_ratio, (in,)).
direction(medium_ratio, (in,)).
direction(high_ratio, (in,)).
direction(very_high_ratio, (in,)).
direction(very_high_interest, (in,)).
direction(high_interest, (in,)).
direction(medium_high_interest, (in,)).
direction(medium_interest, (in,)).
direction(low_interest, (in,)).
direction(short_history, (in,)).
direction(medium_history, (in,)).
direction(long_history, (in,)).
direction(junior_experience, (in,)).
direction(mid_experience, (in,)).
direction(senior_experience, (in,)).
direction(high_school, (in,)).
direction(associate_degree, (in,)).
direction(bachelor_degree, (in,)).
direction(master_degree, (in,)).
direction(doctorate, (in,)).
direction(debt_consolidation, (in,)).
direction(education_loan, (in,)).
direction(medical_loan, (in,)).
direction(personal_loan, (in,)).
direction(venture_capital, (in,)).
direction(home_improvement, (in,)).
direction(male, (in,)).
direction(female, (in,)).
direction(has_default, (in,)).
direction(no_default, (in,)).
direction(renter, (in,)).
direction(owner, (in,)).
direction(high_risk, (in,)).
direction(low_risk, (in,)).
