% solution(Queens) ako je Queens lista polo�aja kraljica koje se ne napadaju
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
% safe(Queens) ako je Queens lista polo�aja kraljica koje se ne napadaju
safe([]).

safe([Queen|Others]) :-
 safe(Others),
 noattack(Queen,Others,1).		% Kako polo�aji redaka nisu zapisani gledamo jeli razlika izme�u stupaca jednaka 1								
noattack(_,[],_).

noattack(Y,[Y1|Ylist],Xdist) :-
 Y1-Y=\=Xdist,				% razlika izme�u stupaca mora biti Xdist koji kre�e s jedan
 Y-Y1=\=Xdist,
 Dist1 is Xdist + 1,			% razlika sljede�e kraljice mora biti Xdist koji je ve�i za jedan od prethodnog 								
 noattack(Y,Ylist,Dist1).