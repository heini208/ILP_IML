max_vars(5).
max_body(3).

head_pred(loan_approved,1).

body_pred(very_young,1).
body_pred(young,1).
body_pred(middle_aged,1).
body_pred(senior,1).
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

% Category Constraints
:- very_young, young.
:- very_young, middle_aged.
:- very_young, senior.
:- young, middle_aged.
:- young, senior.
:- middle_aged, senior.
:- very_small_loan, small_loan.
:- very_small_loan, medium_loan.
:- very_small_loan, large_loan.
:- very_small_loan, very_large_loan.
:- small_loan, medium_loan.
:- small_loan, large_loan.
:- small_loan, very_large_loan.
:- medium_loan, large_loan.
:- medium_loan, very_large_loan.
:- large_loan, very_large_loan.
:- very_low_ratio, low_ratio.
:- very_low_ratio, medium_ratio.
:- very_low_ratio, high_ratio.
:- very_low_ratio, very_high_ratio.
:- low_ratio, medium_ratio.
:- low_ratio, high_ratio.
:- low_ratio, very_high_ratio.
:- medium_ratio, high_ratio.
:- medium_ratio, very_high_ratio.
:- high_ratio, very_high_ratio.
:- very_high_interest, high_interest.
:- very_high_interest, medium_high_interest.
:- very_high_interest, medium_interest.
:- very_high_interest, low_interest.
:- high_interest, medium_high_interest.
:- high_interest, medium_interest.
:- high_interest, low_interest.
:- medium_high_interest, medium_interest.
:- medium_high_interest, low_interest.
:- medium_interest, low_interest.

% Direction of predicates
direction(loan_approved,(in,)).
direction(applicant,(in,)).
direction(very_young,(in,)).
direction(young,(in,)).
direction(middle_aged,(in,)).
direction(senior,(in,)).
direction(very_small_loan,(in,)).
direction(small_loan,(in,)).
direction(medium_loan,(in,)).
direction(large_loan,(in,)).
direction(very_large_loan,(in,)).
direction(very_low_ratio,(in,)).
direction(low_ratio,(in,)).
direction(medium_ratio,(in,)).
direction(high_ratio,(in,)).
direction(very_high_ratio,(in,)).
direction(very_high_interest,(in,)).
direction(high_interest,(in,)).
direction(medium_high_interest,(in,)).
direction(medium_interest,(in,)).
direction(low_interest,(in,)).
direction(high_school,(in,)).
direction(associate_degree,(in,)).
direction(bachelor_degree,(in,)).
direction(master_degree,(in,)).
direction(doctorate,(in,)).
direction(debt_consolidation,(in,)).
direction(education_loan,(in,)).
direction(medical_loan,(in,)).
direction(personal_loan,(in,)).
direction(venture_capital,(in,)).
direction(home_improvement,(in,)).
direction(male,(in,)).
direction(female,(in,)).
direction(has_default,(in,)).
direction(no_default,(in,)).
direction(renter,(in,)).
direction(owner,(in,)).
direction(high_risk,(in,)).
direction(low_risk,(in,)).

% Type definitions
type(loan_approved,(applicant,)).
type(applicant,(applicant,)).
type(very_young,(applicant,)).
type(young,(applicant,)).
type(middle_aged,(applicant,)).
type(senior,(applicant,)).
type(very_small_loan,(applicant,)).
type(small_loan,(applicant,)).
type(medium_loan,(applicant,)).
type(large_loan,(applicant,)).
type(very_large_loan,(applicant,)).
type(very_low_ratio,(applicant,)).
type(low_ratio,(applicant,)).
type(medium_ratio,(applicant,)).
type(high_ratio,(applicant,)).
type(very_high_ratio,(applicant,)).
type(very_high_interest,(applicant,)).
type(high_interest,(applicant,)).
type(medium_high_interest,(applicant,)).
type(medium_interest,(applicant,)).
type(low_interest,(applicant,)).
type(high_school,(applicant,)).
type(associate_degree,(applicant,)).
type(bachelor_degree,(applicant,)).
type(master_degree,(applicant,)).
type(doctorate,(applicant,)).
type(debt_consolidation,(applicant,)).
type(education_loan,(applicant,)).
type(medical_loan,(applicant,)).
type(personal_loan,(applicant,)).
type(venture_capital,(applicant,)).
type(home_improvement,(applicant,)).
type(male,(applicant,)).
type(female,(applicant,)).
type(has_default,(applicant,)).
type(no_default,(applicant,)).
type(renter,(applicant,)).
type(owner,(applicant,)).
type(high_risk,(applicant,)).
type(low_risk,(applicant,)).
