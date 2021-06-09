grammar logo3d;

root : expr+ EOF ;

args : (op (',' op)*)? ;

call : ID '('args')'
     | MAIN
     ;

expr : call                             #CALLPROC
     | PROC MAIN IS block END           #MAIN
     | PROC  ID '('args')' IS block END #PROC
     ;

block : action+;

action : ID ASSIGN op                         #ASSIGN
       | WRITE op                             #WRITE
       | IF comp THEN block (ELSE block)? END #IF
       | WHILE comp DO block END              #WHILE
       | FOR ID FROM op TO op DO block END    #FOR
       | READ ID                              #READ
       | COLOR '(' op ',' op ',' op ')'       #COLOR
       | FORWARD  '('op')'                    #FORWARD
       | BACKWARD '('op')'                    #BACKWARD
       | LEFT '('op')'                        #LEFT
       | RIGHT '('op')'                       #RIGHT
       | UP '('op')'                          #UP
       | DOWN '('op')'                        #DOWN
       | HOME                                 #HOME
       | HIDE                                 #HIDE
       | SHOW                                 #SHOW
       | call                                 #CALLACTION
       ;

comp : op EQ  op #EQ
     | op GT  op #GT
     | op GTE op #GTE
     | op LT  op #LT
     | op LTE op #LTE
     | op DIF op #DIF
     ;

integernumber : ('-')? INT
              | ('+')? INT
              ;

floatnumber : ('-')? FLOAT
            | ('+')? FLOAT
            ;

op : '(' op ')'              #BRACKETS
   | <assoc=right> op POT op #POT
   | op MULT op              #MULT
   | op DIV op               #DIV
   | op SUM op               #SUM
   | op SUB op               #SUB
   | ID                      #ID
   | integernumber           #INT
   | floatnumber             #FLOAT
   ;

SUM  : '+' ;
SUB  : '-' ;
MULT : '*' ;
DIV  : '/' ;
POT  : '^' ;

READ  : '>>' ;
WRITE : '<<' ;

EQ  : '==' ;
GT  : '>'  ;
LT  : '<'  ;
GTE : '>=' ;
LTE : '<=' ;
DIF : '!=' ;

ASSIGN : ':='     ;
IF     : 'IF'     ;
WHILE  : 'WHILE'  ;
MAIN   : 'main()' ;
PROC   : 'PROC'   ;
FOR    : 'FOR'    ;
FROM   : 'FROM'   ;
TO     : 'TO'     ;
DO     : 'DO'     ;
IS     : 'IS'     ;
ELSE   : 'ELSE'   ;
THEN   : 'THEN'   ;

COLOR    : 'color'    ;
FORWARD  : 'forward'  ;
BACKWARD : 'backward' ;
LEFT     : 'left'     ;
RIGHT    : 'right'    ;
UP       : 'up'       ;
DOWN     : 'down'     ;
HOME     : 'home()'   ;
HIDE     : 'hide()'   ;
SHOW     : 'show()'   ;

END      : 'END'      ;

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT : [0-9]+                  ;

FLOAT : [0-9]+ '.' [0-9]*
      | '.' [0-9]+
      ;

COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \n\r]+ -> skip      ;