max_rules(7).     
max_literals(5).  
max_body(4).     
max_vars(5).    


head_pred(survived,1).

body_pred(pclass,2).
body_pred(sex,2).
body_pred(age,2).
body_pred(sibsp,2).
body_pred(parch,2).
body_pred(fare,2).
body_pred(embarked,2).
body_pred(passenger,1).

% Types
type(survived,(passenger,)).
type(pclass,(passenger,real)).
type(sex,(passenger,string)).
type(age,(passenger,real)).
type(sibsp,(passenger,real)).
type(parch,(passenger,real)).
type(fare,(passenger,real)).
type(embarked,(passenger,string)).
type(passenger,(passenger,)).

% Directions
direction(survived,(in,)).
direction(pclass,(in,out)).
direction(sex,(in,out)).
direction(age,(in,out)).
direction(sibsp,(in,out)).
direction(parch,(in,out)).
direction(fare,(in,out)).
direction(embarked,(in,out)).
direction(passenger,(in,)).

:-
    clause(C),
    #count{V : var_type(C,V,passenger)} != 1.