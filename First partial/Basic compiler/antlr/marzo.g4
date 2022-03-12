grammar marzo;

program: expr+;

// General expression
expr: 
    arith_expr # arithExpr
    | relational_expr # relationalExpr
    | logical_expr #logicalExpr
    | comp_expr # compExpr
    ;

// Types of expressions (arithmetic, relational, logical, complex)
arith_expr:
    arith_expr '+' arith_expr                               # add
    | arith_expr '-' arith_expr                             # sub
    | INTEGER_NUMBER                                    # intNumber
    ; 

relational_expr:
    declaration  # declare
    | assignment # assign
    ;

logical_expr: 
    logical_expr 'and' logical_expr #andCond
    | logical_expr 'or' logical_expr #orCond
    | 'not' logical_expr #notCond
    | logical_expr '>=' logical_expr #goeCond
    | logical_expr '<=' logical_expr #loeCond
    | logical_expr '>' logical_expr #gCond
    | logical_expr '<' logical_expr #lCond
    | IDENTIFIER # identCond
    | INTEGER_NUMBER #intNumberCond
    ;

comp_expr:
    'if (' logical_expr ') then' expr+ 'end' # ifnoelse
    | 'if (' logical_expr ') then' expr+ 'else' expr+ 'end' # ifelse
    | print_op # print
    ;  

// Utils
print_op: 
    'print(' (INTEGER_NUMBER | IDENTIFIER)+ ')'
    ;

assignment:
    IDENTIFIER ASSIGN arith_expr
    ; 

declaration: 
    KEYWORD IDENTIFIER                               
    ;                             

KEYWORD: 'int' | 'double' | 'char';
ASSIGN: '=';
IDENTIFIER: ALPHA;
ALPHA: [a-zA-Z_$] [a-zA-Z_$0-9]* ;
INTEGER_NUMBER: [0-9]+;

WS : [ \t\n\r]+ -> skip;