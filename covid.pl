/* PB1 Abhishek Wahane */

/* Covid Test Expert System */

check:-
diagnose(Corona),
write('This Person '),
write(Corona),
nl,
write('Please go into Quarantine.'),
undo.

diagnose("should get tested for covid") :- covid, !.
diagnose("does not have Covid").

/*Rules*/
covid :-
verify("Cough"),
verify("Headache"),
verify("High Fever"),
verify("Difficulty in Breathing").
       
/* Questions */
ask(Question) :-
write('Does the person have '),
write(Question),
write('? '),
read(Response),
nl,
( (Response == yes ; Response == y)
->
assert(yes(Question)) ;
assert(no(Question)), fail).

:- dynamic yes/1,no/1.
verify(S) :-
(yes(S)
->
true ;
(no(S)
->
fail ;
ask(S))).
undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.









/*

OUTPUT:

/Users/abhi/covid.pl compiled, 46 lines read - 1402 bytes written, 4 ms

(1 ms) yes
check.

Does the person have Cough?
yes

Does the person have Headache?
yes

Does the person have High Fever?
yes

Does the person have Difficulty in Breathing?
yes

This Person should get tested for covid
Please go into Quarantine.
1true

*/
