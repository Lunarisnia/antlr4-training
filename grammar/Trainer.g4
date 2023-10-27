grammar Trainer;

fragment RAW_STRING:
    (. | ~[\n\r]);

fragment SINGLE_LINE_STRING :
    '"' (RAW_STRING | ~["])*? '"';

WS: [ \t\n\r\f]+ -> skip ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
STRING: SINGLE_LINE_STRING;

program : (func)* EOF;

func : ID '<' STRING '>';