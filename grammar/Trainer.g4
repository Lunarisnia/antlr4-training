grammar Trainer;

fragment RAW_STRING: (. | ~[\n\r]);

fragment SINGLE_LINE_STRING: '"' (RAW_STRING | ~["])*? '"';

WS: [ \t\n\r\f]+ -> skip;
STRING: SINGLE_LINE_STRING {self.text = self.text[1:-1]};
TRUE: 'T';
FALSE: 'F';
ADD: '+';
SUBTRACT: '-';
MULTIPLY: '*';
DIVIDE: '/';

INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;

program: (func | var)* EOF;

func: ID '<' STRING '>';

atom: INT | TRUE | FALSE | STRING;
calculation:
	INT (ADD | SUBTRACT | DIVIDE | MULTIPLY) INT
	| ID (ADD | SUBTRACT | DIVIDE | MULTIPLY) ID;
expr: atom | calculation;
var: ID '=' (expr | ID);