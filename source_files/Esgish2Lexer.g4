lexer grammar Esgish2Lexer;

// Lexer rules
// SAVED_SCREEN needs to be before FACTOR to get recognized first
SAVED_SCREEN: BO 'screen#' ('0'..'9') + BC ;
FACTOR: BO ( 'a'..'z' | 'A'..'Z' | '0'..'9' | '&' | '#' ) + BC ;
CUSTOM_SCORE: BO ('rel~' [0-9]+ '~')? UUID128 BC ;
OP_NULL_TYPE: 'IS' ;
OP_BOOLEAN: ('True' | 'False') ;
OP_ORDER: '=='|'<='|'>='|'<'|'>'|'!=' ;
OP_STRING_MATCH: ('CTN'|'LCTN'|'STW' ) ;
OP_STRING_LIST: ('ANY' | 'NONE' | 'ALL' | 'IN' ) ;
OP_STRING_MAP: ('ANY_MAP' ) ;
OP_STRING_LIST_NO_ARG: 'EMPTY' ;
OP_DATE: ( 'PRE' | 'PST' ) ;

// formulas
CASE_COUNT: 'CASE_COUNT';
IF: 'IF';
PERSON_COUNT: 'PERSON_COUNT' ;
PERCENTILE_RANK_IN_CATEGORY: 'PERCENTILE_RANK_IN_CATEGORY' ;
PERCENTILE_RANK: 'PERCENTILE_RANK' ;
QUANTILE: 'QUANTILE';
QUANTILE_IN_CATEGORY: 'QUANTILE_IN_CATEGORY';
RANK_ASCENDING: 'RANK_ASCENDING';
RANK_DESCENDING: 'RANK_DESCENDING';
SUM: 'SUM' ;
DIFFERENCE: 'DIFFERENCE' ;
COALESCE: 'COALESCE';
RATIO: 'RATIO';
YEARS_SINCE: 'YEARS_SINCE';
BOOLEAN: 'BOOLEAN';

AND: 'AND';
OR: 'OR';
NOT: 'NOT';
BO: '[';
BC: ']';

NULL: 'NULL';
NULL_LIST: (':NC' | ':NI' | ':NA' | ':NM' | ':ND')+;
ARG: QT ( ESC_SINGLE_QUOTE | LETTER | DIGIT | ' ' | DASH | '+' | '*' | DOT | ','| '&' | '$' | '%' | '/' | '<' | '>' | '|' | ':' | '(' | ')' | '[' | ']' )* QT ;
WS: [ \t\r\n]+ -> skip;

// fragments--not recognized by parser
fragment DIGIT: '0'..'9' ;
fragment LETTER: [a-zA-Z] ;
fragment HEX: [0-9a-fA-F];
fragment UUID128:  HEX HEX HEX HEX HEX HEX HEX HEX DASH
                   HEX HEX HEX HEX DASH
                   HEX HEX HEX HEX DASH
                   HEX HEX HEX HEX DASH
                   HEX HEX HEX HEX HEX HEX HEX HEX HEX HEX HEX HEX ;
fragment DASH: '-' ;
fragment DOT: '.' ;
fragment QT: '\'';
fragment ESC_SINGLE_QUOTE: '\\\'' ;
