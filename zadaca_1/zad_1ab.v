Set Implicit Arguments.
Require Import Bool.


Notation "! A" := (negb A) (at level 20, right associativity).
Lemma Zad1a (X Y : bool) :
  (X && !Y) || (!X && !Y) || (!X && Y) = (!X || !Y).
Proof.
  destruct X, Y; simpl; reflexivity.
Qed.

Lemma Zad1b (X Y Z : bool) :
  !(!X && Y && Z) && !(X && Y && !Z) && (X && !Y && Z) = (X && !Y && Z).
Proof. 
  destruct X,Y,Z; simpl; try reflexivity. 
Qed.






