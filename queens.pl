% solution(Queens) ako je Queens lista položaja kraljica koje se ne napadaju
solution(Queens) :-
 permutation([1,2,3,4,5,6,7,8], Queens),	% permutacije liste od 1-8 koja se sprema u Queens
 safe(Queens).

% permutacija
permutation([],[]).

permutation([Head|Tail],PermList) :-
 permutation(Tail,PermTail),
 del(Head,PermList,PermTail).

del(Item,[Item|List],List).

del(Item,[First|List],[First|List1]) :-
 del(Item,List,List1).
% safe(Queens) ako je Queens lista položaja kraljica koje se ne napadaju
safe([]).

safe([Queen|Others]) :-
 safe(Others),
 noattack(Queen,Others,1).		% Kako položaji redaka nisu zapisani gledamo jeli razlika izmeðu stupaca jednaka 1								
noattack(_,[],_).

noattack(Y,[Y1|Ylist],Xdist) :-
 Y1-Y=\=Xdist,				% razlika izmeðu stupaca mora biti Xdist koji kreæe s jedan
 Y-Y1=\=Xdist,
 Dist1 is Xdist + 1,			% razlika sljedeæe kraljice mora biti Xdist koji je veæi za jedan od prethodnog 								
 noattack(Y,Ylist,Dist1).