grammar Esgish2Grammar;

import Esgish2Lexer;

start: ( query | wrappedQuery | formula) EOF ;

query:
    ( singleFactorQuery
    | andQuery
    | orQuery
    | negatedQuery
    | savedQuery
    | customScoreQuery
    )
    ;
wrappedQuery: '(' ( query | wrappedQuery ) ')';

singleFactorQuery:
  (
    booleanQuery
  | customScoreQuery
  | dateQuery
  | formulaQuery
  | nullTypeQuery
  | numberOrStringQuery
  | stringListQuery
  | stringMapQuery
  | stringQuery
  | negatedQuery
 )
 ;

// single factor filters
booleanQuery: FACTOR OP_BOOLEAN NULL_LIST?;
dateQuery: FACTOR OP_DATE ARG NULL_LIST?;
formulaQuery: formula OP_ORDER ARG NULL_LIST?;
nullTypeQuery: FACTOR OP_NULL_TYPE (NULL_LIST? | NULL);
numberOrStringQuery: FACTOR OP_ORDER ARG NULL_LIST?;
stringListQuery: (FACTOR OP_STRING_LIST ARG | FACTOR OP_STRING_LIST_NO_ARG ) NULL_LIST?;
stringMapQuery: FACTOR OP_STRING_MAP ARG NULL_LIST?;
stringQuery: FACTOR OP_STRING_MATCH ARG NULL_LIST?;

savedQuery: SAVED_SCREEN OP_BOOLEAN ;
wrappedSavedQuery: '(' ( savedQuery | wrappedSavedQuery ) ')';

customScoreQuery: CUSTOM_SCORE OP_ORDER ARG ;

andQuery: AND '('  groupQueryElement (',' groupQueryElement)+ ')';
orQuery: OR '('  groupQueryElement (',' groupQueryElement)+ ')';
negatedQuery: NOT wrappedQuery;

groupQueryElement: (singleFactorQuery
  | andQuery
  | negatedQuery
  | orQuery
  | savedQuery
  | formula) ;

formula:
  (
  caseCountFormula
  | ifFormula
  | personCountFormula
  | percentileRankFormula
  | percentileRankInCategoryFormula
  | quantileFormula
  | quantileFormulaInCategoryFormula
  | rankAscendingFormula
  | rankDescendingFormula
  | sumFormula
  | differenceFormula
  | coalesceFormula
  | ratioFormula
  | yearsSinceFormula
  | booleanFormula
  ) ;

ratioFormula: RATIO '('FACTOR','FACTOR')';
coalesceFormula: COALESCE '('FACTOR','FACTOR')';
caseCountFormula: CASE_COUNT '(' query ')' ;
ifFormula: IF '(' (singleFactorQuery ',' (ARG | NULL_LIST) ',')+ (ARG | NULL_LIST) ')';
personCountFormula: PERSON_COUNT '(' query ')' ;
percentileRankFormula: PERCENTILE_RANK '(' FACTOR ')' ;
percentileRankInCategoryFormula: PERCENTILE_RANK_IN_CATEGORY '(' FACTOR ',' FACTOR ')' ;
quantileFormula: QUANTILE '(' FACTOR ',' ARG ')' ;
quantileFormulaInCategoryFormula: QUANTILE_IN_CATEGORY '(' FACTOR ',' FACTOR ',' ARG ')' ;
rankAscendingFormula: RANK_ASCENDING '(' FACTOR ')' ;
rankDescendingFormula: RANK_DESCENDING '(' FACTOR ')' ;
sumFormula: SUM '(' FACTOR (',' FACTOR)+ ')' ;
differenceFormula: DIFFERENCE '(' FACTOR (',' FACTOR)+ ')' ;
yearsSinceFormula: YEARS_SINCE '(' FACTOR ')' ;
booleanFormula: BOOLEAN '(' query ')';