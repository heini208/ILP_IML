max_rules(5).     
max_literals(8).  
max_body(10).      
max_vars(10).    

head_pred(survived,1).

body_pred(pclass,2).
body_pred(sex_male,1).
body_pred(sex_female,1).
body_pred(age,2).
body_pred(child,1).
body_pred(adult,1).
body_pred(elderly,1).
body_pred(fare,2).
body_pred(high_fare,1).
body_pred(low_fare,1).
body_pred(embarked_c,1).
body_pred(embarked_q,1). 
body_pred(embarked_s,1). 
body_pred(sibsp,2).
body_pred(parch,2).

type(survived, (passenger,)).
type(pclass, (passenger, real)).
type(sex_male, (passenger,)).  
type(sex_female, (passenger,)).  
type(age, (passenger, real)).
type(child, (passenger,)).
type(adult, (passenger,)).
type(elderly, (passenger,)).
type(fare, (passenger, real)).
type(high_fare, (passenger,)).
type(low_fare, (passenger,)).


type(embarked_c, (passenger,)).  
type(embarked_q, (passenger,)).  
type(embarked_s, (passenger,)).  
type(sibsp, (passenger, real)).
type(parch, (passenger, real)).
type(passenger, (passenger,)).

direction(survived, (in,)).
direction(pclass, (in,out)).
direction(sex_male, (in,)).  
direction(sex_female, (in,)).  
direction(age, (in,out)).  
direction(child, (in,)).
direction(adult, (in,)).
direction(elderly, (in,)).
direction(fare, (in,out)).
direction(high_fare, (in,)).
direction(low_fare, (in,)).
direction(embarked_c, (in,)).
direction(embarked_q, (in,)). 
direction(embarked_s, (in,)). 
direction(sibsp, (in,out)).
direction(parch, (in,out)).

enable_pi.