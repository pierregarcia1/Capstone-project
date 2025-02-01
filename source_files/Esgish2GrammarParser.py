# Generated from Esgish2Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing import TextIO

def serializedATN():
    return [
        4,1,38,330,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,3,0,74,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,84,8,1,1,2,1,2,1,2,3,2,89,8,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,1,4,3,4,108,8,4,1,5,
        1,5,1,5,1,5,3,5,114,8,5,1,6,1,6,1,6,1,6,3,6,120,8,6,1,7,1,7,1,7,
        3,7,125,8,7,1,7,3,7,128,8,7,1,8,1,8,1,8,1,8,3,8,134,8,8,1,9,1,9,
        1,9,1,9,1,9,3,9,141,8,9,1,9,3,9,144,8,9,1,10,1,10,1,10,1,10,3,10,
        150,8,10,1,11,1,11,1,11,1,11,3,11,156,8,11,1,12,1,12,1,12,1,13,1,
        13,1,13,3,13,164,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,4,15,177,8,15,11,15,12,15,178,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,4,16,188,8,16,11,16,12,16,189,1,16,1,16,1,17,1,17,1,
        17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,203,8,18,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,220,
        8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,4,23,248,8,23,11,23,12,23,249,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,31,1,31,1,31,1,31,1,31,4,31,303,8,31,11,31,12,31,304,1,31,
        1,31,1,32,1,32,1,32,1,32,1,32,4,32,314,8,32,11,32,12,32,315,1,32,
        1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,0,0,
        35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,0,1,1,0,36,37,346,0,73,1,
        0,0,0,2,83,1,0,0,0,4,85,1,0,0,0,6,102,1,0,0,0,8,104,1,0,0,0,10,109,
        1,0,0,0,12,115,1,0,0,0,14,121,1,0,0,0,16,129,1,0,0,0,18,140,1,0,
        0,0,20,145,1,0,0,0,22,151,1,0,0,0,24,157,1,0,0,0,26,160,1,0,0,0,
        28,167,1,0,0,0,30,171,1,0,0,0,32,182,1,0,0,0,34,193,1,0,0,0,36,202,
        1,0,0,0,38,219,1,0,0,0,40,221,1,0,0,0,42,228,1,0,0,0,44,235,1,0,
        0,0,46,240,1,0,0,0,48,254,1,0,0,0,50,259,1,0,0,0,52,264,1,0,0,0,
        54,271,1,0,0,0,56,278,1,0,0,0,58,287,1,0,0,0,60,292,1,0,0,0,62,297,
        1,0,0,0,64,308,1,0,0,0,66,319,1,0,0,0,68,324,1,0,0,0,70,74,3,2,1,
        0,71,74,3,4,2,0,72,74,3,38,19,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,
        1,0,0,0,74,75,1,0,0,0,75,76,5,0,0,1,76,1,1,0,0,0,77,84,3,6,3,0,78,
        84,3,30,15,0,79,84,3,32,16,0,80,84,3,34,17,0,81,84,3,24,12,0,82,
        84,3,28,14,0,83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,
        0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,88,5,1,0,0,86,89,
        3,2,1,0,87,89,3,4,2,0,88,86,1,0,0,0,88,87,1,0,0,0,89,90,1,0,0,0,
        90,91,5,2,0,0,91,5,1,0,0,0,92,103,3,8,4,0,93,103,3,28,14,0,94,103,
        3,10,5,0,95,103,3,12,6,0,96,103,3,14,7,0,97,103,3,16,8,0,98,103,
        3,18,9,0,99,103,3,20,10,0,100,103,3,22,11,0,101,103,3,34,17,0,102,
        92,1,0,0,0,102,93,1,0,0,0,102,94,1,0,0,0,102,95,1,0,0,0,102,96,1,
        0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,
        0,102,101,1,0,0,0,103,7,1,0,0,0,104,105,5,5,0,0,105,107,5,8,0,0,
        106,108,5,36,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,9,1,0,0,0,109,
        110,5,5,0,0,110,111,5,14,0,0,111,113,5,37,0,0,112,114,5,36,0,0,113,
        112,1,0,0,0,113,114,1,0,0,0,114,11,1,0,0,0,115,116,3,38,19,0,116,
        117,5,9,0,0,117,119,5,37,0,0,118,120,5,36,0,0,119,118,1,0,0,0,119,
        120,1,0,0,0,120,13,1,0,0,0,121,122,5,5,0,0,122,127,5,7,0,0,123,125,
        5,36,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,128,1,0,0,0,126,128,
        5,35,0,0,127,124,1,0,0,0,127,126,1,0,0,0,128,15,1,0,0,0,129,130,
        5,5,0,0,130,131,5,9,0,0,131,133,5,37,0,0,132,134,5,36,0,0,133,132,
        1,0,0,0,133,134,1,0,0,0,134,17,1,0,0,0,135,136,5,5,0,0,136,137,5,
        11,0,0,137,141,5,37,0,0,138,139,5,5,0,0,139,141,5,13,0,0,140,135,
        1,0,0,0,140,138,1,0,0,0,141,143,1,0,0,0,142,144,5,36,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,19,1,0,0,0,145,146,5,5,0,0,146,147,5,
        12,0,0,147,149,5,37,0,0,148,150,5,36,0,0,149,148,1,0,0,0,149,150,
        1,0,0,0,150,21,1,0,0,0,151,152,5,5,0,0,152,153,5,10,0,0,153,155,
        5,37,0,0,154,156,5,36,0,0,155,154,1,0,0,0,155,156,1,0,0,0,156,23,
        1,0,0,0,157,158,5,4,0,0,158,159,5,8,0,0,159,25,1,0,0,0,160,163,5,
        1,0,0,161,164,3,24,12,0,162,164,3,26,13,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,165,1,0,0,0,165,166,5,2,0,0,166,27,1,0,0,0,167,168,5,
        6,0,0,168,169,5,9,0,0,169,170,5,37,0,0,170,29,1,0,0,0,171,172,5,
        30,0,0,172,173,5,1,0,0,173,176,3,36,18,0,174,175,5,3,0,0,175,177,
        3,36,18,0,176,174,1,0,0,0,177,178,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,180,1,0,0,0,180,181,5,2,0,0,181,31,1,0,0,0,182,183,5,
        31,0,0,183,184,5,1,0,0,184,187,3,36,18,0,185,186,5,3,0,0,186,188,
        3,36,18,0,187,185,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,191,1,0,0,0,191,192,5,2,0,0,192,33,1,0,0,0,193,194,5,
        32,0,0,194,195,3,4,2,0,195,35,1,0,0,0,196,203,3,6,3,0,197,203,3,
        30,15,0,198,203,3,34,17,0,199,203,3,32,16,0,200,203,3,24,12,0,201,
        203,3,38,19,0,202,196,1,0,0,0,202,197,1,0,0,0,202,198,1,0,0,0,202,
        199,1,0,0,0,202,200,1,0,0,0,202,201,1,0,0,0,203,37,1,0,0,0,204,220,
        3,44,22,0,205,220,3,46,23,0,206,220,3,48,24,0,207,220,3,50,25,0,
        208,220,3,52,26,0,209,220,3,54,27,0,210,220,3,56,28,0,211,220,3,
        58,29,0,212,220,3,60,30,0,213,220,3,62,31,0,214,220,3,64,32,0,215,
        220,3,42,21,0,216,220,3,40,20,0,217,220,3,66,33,0,218,220,3,68,34,
        0,219,204,1,0,0,0,219,205,1,0,0,0,219,206,1,0,0,0,219,207,1,0,0,
        0,219,208,1,0,0,0,219,209,1,0,0,0,219,210,1,0,0,0,219,211,1,0,0,
        0,219,212,1,0,0,0,219,213,1,0,0,0,219,214,1,0,0,0,219,215,1,0,0,
        0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,39,1,0,0,0,
        221,222,5,27,0,0,222,223,5,1,0,0,223,224,5,5,0,0,224,225,5,3,0,0,
        225,226,5,5,0,0,226,227,5,2,0,0,227,41,1,0,0,0,228,229,5,26,0,0,
        229,230,5,1,0,0,230,231,5,5,0,0,231,232,5,3,0,0,232,233,5,5,0,0,
        233,234,5,2,0,0,234,43,1,0,0,0,235,236,5,15,0,0,236,237,5,1,0,0,
        237,238,3,2,1,0,238,239,5,2,0,0,239,45,1,0,0,0,240,241,5,16,0,0,
        241,247,5,1,0,0,242,243,3,6,3,0,243,244,5,3,0,0,244,245,7,0,0,0,
        245,246,5,3,0,0,246,248,1,0,0,0,247,242,1,0,0,0,248,249,1,0,0,0,
        249,247,1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,251,252,7,0,0,0,
        252,253,5,2,0,0,253,47,1,0,0,0,254,255,5,17,0,0,255,256,5,1,0,0,
        256,257,3,2,1,0,257,258,5,2,0,0,258,49,1,0,0,0,259,260,5,19,0,0,
        260,261,5,1,0,0,261,262,5,5,0,0,262,263,5,2,0,0,263,51,1,0,0,0,264,
        265,5,18,0,0,265,266,5,1,0,0,266,267,5,5,0,0,267,268,5,3,0,0,268,
        269,5,5,0,0,269,270,5,2,0,0,270,53,1,0,0,0,271,272,5,20,0,0,272,
        273,5,1,0,0,273,274,5,5,0,0,274,275,5,3,0,0,275,276,5,37,0,0,276,
        277,5,2,0,0,277,55,1,0,0,0,278,279,5,21,0,0,279,280,5,1,0,0,280,
        281,5,5,0,0,281,282,5,3,0,0,282,283,5,5,0,0,283,284,5,3,0,0,284,
        285,5,37,0,0,285,286,5,2,0,0,286,57,1,0,0,0,287,288,5,22,0,0,288,
        289,5,1,0,0,289,290,5,5,0,0,290,291,5,2,0,0,291,59,1,0,0,0,292,293,
        5,23,0,0,293,294,5,1,0,0,294,295,5,5,0,0,295,296,5,2,0,0,296,61,
        1,0,0,0,297,298,5,24,0,0,298,299,5,1,0,0,299,302,5,5,0,0,300,301,
        5,3,0,0,301,303,5,5,0,0,302,300,1,0,0,0,303,304,1,0,0,0,304,302,
        1,0,0,0,304,305,1,0,0,0,305,306,1,0,0,0,306,307,5,2,0,0,307,63,1,
        0,0,0,308,309,5,25,0,0,309,310,5,1,0,0,310,313,5,5,0,0,311,312,5,
        3,0,0,312,314,5,5,0,0,313,311,1,0,0,0,314,315,1,0,0,0,315,313,1,
        0,0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,318,5,2,0,0,318,65,1,0,
        0,0,319,320,5,28,0,0,320,321,5,1,0,0,321,322,5,5,0,0,322,323,5,2,
        0,0,323,67,1,0,0,0,324,325,5,29,0,0,325,326,5,1,0,0,326,327,3,2,
        1,0,327,328,5,2,0,0,328,69,1,0,0,0,22,73,83,88,102,107,113,119,124,
        127,133,140,143,149,155,163,178,189,202,219,249,304,315
    ]

class Esgish2GrammarParser ( Parser ):

    grammarFileName = "Esgish2Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'IS'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'EMPTY'", "<INVALID>", "'CASE_COUNT'", 
                     "'IF'", "'PERSON_COUNT'", "'PERCENTILE_RANK_IN_CATEGORY'", 
                     "'PERCENTILE_RANK'", "'QUANTILE'", "'QUANTILE_IN_CATEGORY'", 
                     "'RANK_ASCENDING'", "'RANK_DESCENDING'", "'SUM'", "'DIFFERENCE'", 
                     "'COALESCE'", "'RATIO'", "'YEARS_SINCE'", "'BOOLEAN'", 
                     "'AND'", "'OR'", "'NOT'", "'['", "']'", "'NULL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SAVED_SCREEN", "FACTOR", "CUSTOM_SCORE", "OP_NULL_TYPE", 
                      "OP_BOOLEAN", "OP_ORDER", "OP_STRING_MATCH", "OP_STRING_LIST", 
                      "OP_STRING_MAP", "OP_STRING_LIST_NO_ARG", "OP_DATE", 
                      "CASE_COUNT", "IF", "PERSON_COUNT", "PERCENTILE_RANK_IN_CATEGORY", 
                      "PERCENTILE_RANK", "QUANTILE", "QUANTILE_IN_CATEGORY", 
                      "RANK_ASCENDING", "RANK_DESCENDING", "SUM", "DIFFERENCE", 
                      "COALESCE", "RATIO", "YEARS_SINCE", "BOOLEAN", "AND", 
                      "OR", "NOT", "BO", "BC", "NULL", "NULL_LIST", "ARG", 
                      "WS" ]

    RULE_start = 0
    RULE_query = 1
    RULE_wrappedQuery = 2
    RULE_singleFactorQuery = 3
    RULE_booleanQuery = 4
    RULE_dateQuery = 5
    RULE_formulaQuery = 6
    RULE_nullTypeQuery = 7
    RULE_numberOrStringQuery = 8
    RULE_stringListQuery = 9
    RULE_stringMapQuery = 10
    RULE_stringQuery = 11
    RULE_savedQuery = 12
    RULE_wrappedSavedQuery = 13
    RULE_customScoreQuery = 14
    RULE_andQuery = 15
    RULE_orQuery = 16
    RULE_negatedQuery = 17
    RULE_groupQueryElement = 18
    RULE_formula = 19
    RULE_ratioFormula = 20
    RULE_coalesceFormula = 21
    RULE_caseCountFormula = 22
    RULE_ifFormula = 23
    RULE_personCountFormula = 24
    RULE_percentileRankFormula = 25
    RULE_percentileRankInCategoryFormula = 26
    RULE_quantileFormula = 27
    RULE_quantileFormulaInCategoryFormula = 28
    RULE_rankAscendingFormula = 29
    RULE_rankDescendingFormula = 30
    RULE_sumFormula = 31
    RULE_differenceFormula = 32
    RULE_yearsSinceFormula = 33
    RULE_booleanFormula = 34

    ruleNames =  [ "start", "query", "wrappedQuery", "singleFactorQuery", 
                   "booleanQuery", "dateQuery", "formulaQuery", "nullTypeQuery", 
                   "numberOrStringQuery", "stringListQuery", "stringMapQuery", 
                   "stringQuery", "savedQuery", "wrappedSavedQuery", "customScoreQuery", 
                   "andQuery", "orQuery", "negatedQuery", "groupQueryElement", 
                   "formula", "ratioFormula", "coalesceFormula", "caseCountFormula", 
                   "ifFormula", "personCountFormula", "percentileRankFormula", 
                   "percentileRankInCategoryFormula", "quantileFormula", 
                   "quantileFormulaInCategoryFormula", "rankAscendingFormula", 
                   "rankDescendingFormula", "sumFormula", "differenceFormula", 
                   "yearsSinceFormula", "booleanFormula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SAVED_SCREEN=4
    FACTOR=5
    CUSTOM_SCORE=6
    OP_NULL_TYPE=7
    OP_BOOLEAN=8
    OP_ORDER=9
    OP_STRING_MATCH=10
    OP_STRING_LIST=11
    OP_STRING_MAP=12
    OP_STRING_LIST_NO_ARG=13
    OP_DATE=14
    CASE_COUNT=15
    IF=16
    PERSON_COUNT=17
    PERCENTILE_RANK_IN_CATEGORY=18
    PERCENTILE_RANK=19
    QUANTILE=20
    QUANTILE_IN_CATEGORY=21
    RANK_ASCENDING=22
    RANK_DESCENDING=23
    SUM=24
    DIFFERENCE=25
    COALESCE=26
    RATIO=27
    YEARS_SINCE=28
    BOOLEAN=29
    AND=30
    OR=31
    NOT=32
    BO=33
    BC=34
    NULL=35
    NULL_LIST=36
    ARG=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Esgish2GrammarParser.EOF, 0)

        def query(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QueryContext,0)


        def wrappedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.WrappedQueryContext,0)


        def formula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = Esgish2GrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 70
                self.query()
                pass

            elif la_ == 2:
                self.state = 71
                self.wrappedQuery()
                pass

            elif la_ == 3:
                self.state = 72
                self.formula()
                pass


            self.state = 75
            self.match(Esgish2GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleFactorQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SingleFactorQueryContext,0)


        def andQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.AndQueryContext,0)


        def orQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.OrQueryContext,0)


        def negatedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.NegatedQueryContext,0)


        def savedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SavedQueryContext,0)


        def customScoreQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.CustomScoreQueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = Esgish2GrammarParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 77
                self.singleFactorQuery()
                pass

            elif la_ == 2:
                self.state = 78
                self.andQuery()
                pass

            elif la_ == 3:
                self.state = 79
                self.orQuery()
                pass

            elif la_ == 4:
                self.state = 80
                self.negatedQuery()
                pass

            elif la_ == 5:
                self.state = 81
                self.savedQuery()
                pass

            elif la_ == 6:
                self.state = 82
                self.customScoreQuery()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WrappedQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QueryContext,0)


        def wrappedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.WrappedQueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_wrappedQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrappedQuery" ):
                listener.enterWrappedQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrappedQuery" ):
                listener.exitWrappedQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrappedQuery" ):
                return visitor.visitWrappedQuery(self)
            else:
                return visitor.visitChildren(self)




    def wrappedQuery(self):

        localctx = Esgish2GrammarParser.WrappedQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_wrappedQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(Esgish2GrammarParser.T__0)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
                self.state = 86
                self.query()
                pass
            elif token in [1]:
                self.state = 87
                self.wrappedQuery()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 90
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleFactorQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.BooleanQueryContext,0)


        def customScoreQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.CustomScoreQueryContext,0)


        def dateQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.DateQueryContext,0)


        def formulaQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.FormulaQueryContext,0)


        def nullTypeQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.NullTypeQueryContext,0)


        def numberOrStringQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.NumberOrStringQueryContext,0)


        def stringListQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.StringListQueryContext,0)


        def stringMapQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.StringMapQueryContext,0)


        def stringQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.StringQueryContext,0)


        def negatedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.NegatedQueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_singleFactorQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleFactorQuery" ):
                listener.enterSingleFactorQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleFactorQuery" ):
                listener.exitSingleFactorQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleFactorQuery" ):
                return visitor.visitSingleFactorQuery(self)
            else:
                return visitor.visitChildren(self)




    def singleFactorQuery(self):

        localctx = Esgish2GrammarParser.SingleFactorQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_singleFactorQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 92
                self.booleanQuery()
                pass

            elif la_ == 2:
                self.state = 93
                self.customScoreQuery()
                pass

            elif la_ == 3:
                self.state = 94
                self.dateQuery()
                pass

            elif la_ == 4:
                self.state = 95
                self.formulaQuery()
                pass

            elif la_ == 5:
                self.state = 96
                self.nullTypeQuery()
                pass

            elif la_ == 6:
                self.state = 97
                self.numberOrStringQuery()
                pass

            elif la_ == 7:
                self.state = 98
                self.stringListQuery()
                pass

            elif la_ == 8:
                self.state = 99
                self.stringMapQuery()
                pass

            elif la_ == 9:
                self.state = 100
                self.stringQuery()
                pass

            elif la_ == 10:
                self.state = 101
                self.negatedQuery()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_BOOLEAN(self):
            return self.getToken(Esgish2GrammarParser.OP_BOOLEAN, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_booleanQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanQuery" ):
                listener.enterBooleanQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanQuery" ):
                listener.exitBooleanQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanQuery" ):
                return visitor.visitBooleanQuery(self)
            else:
                return visitor.visitChildren(self)




    def booleanQuery(self):

        localctx = Esgish2GrammarParser.BooleanQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_booleanQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 105
            self.match(Esgish2GrammarParser.OP_BOOLEAN)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 106
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_DATE(self):
            return self.getToken(Esgish2GrammarParser.OP_DATE, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_dateQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateQuery" ):
                listener.enterDateQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateQuery" ):
                listener.exitDateQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateQuery" ):
                return visitor.visitDateQuery(self)
            else:
                return visitor.visitChildren(self)




    def dateQuery(self):

        localctx = Esgish2GrammarParser.DateQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dateQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 110
            self.match(Esgish2GrammarParser.OP_DATE)
            self.state = 111
            self.match(Esgish2GrammarParser.ARG)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 112
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.FormulaContext,0)


        def OP_ORDER(self):
            return self.getToken(Esgish2GrammarParser.OP_ORDER, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_formulaQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormulaQuery" ):
                listener.enterFormulaQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormulaQuery" ):
                listener.exitFormulaQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormulaQuery" ):
                return visitor.visitFormulaQuery(self)
            else:
                return visitor.visitChildren(self)




    def formulaQuery(self):

        localctx = Esgish2GrammarParser.FormulaQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formulaQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.formula()
            self.state = 116
            self.match(Esgish2GrammarParser.OP_ORDER)
            self.state = 117
            self.match(Esgish2GrammarParser.ARG)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 118
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullTypeQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_NULL_TYPE(self):
            return self.getToken(Esgish2GrammarParser.OP_NULL_TYPE, 0)

        def NULL(self):
            return self.getToken(Esgish2GrammarParser.NULL, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_nullTypeQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullTypeQuery" ):
                listener.enterNullTypeQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullTypeQuery" ):
                listener.exitNullTypeQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullTypeQuery" ):
                return visitor.visitNullTypeQuery(self)
            else:
                return visitor.visitChildren(self)




    def nullTypeQuery(self):

        localctx = Esgish2GrammarParser.NullTypeQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nullTypeQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 122
            self.match(Esgish2GrammarParser.OP_NULL_TYPE)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 2, 3, 36]:
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 123
                    self.match(Esgish2GrammarParser.NULL_LIST)


                pass
            elif token in [35]:
                self.state = 126
                self.match(Esgish2GrammarParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberOrStringQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_ORDER(self):
            return self.getToken(Esgish2GrammarParser.OP_ORDER, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_numberOrStringQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberOrStringQuery" ):
                listener.enterNumberOrStringQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberOrStringQuery" ):
                listener.exitNumberOrStringQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberOrStringQuery" ):
                return visitor.visitNumberOrStringQuery(self)
            else:
                return visitor.visitChildren(self)




    def numberOrStringQuery(self):

        localctx = Esgish2GrammarParser.NumberOrStringQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_numberOrStringQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 130
            self.match(Esgish2GrammarParser.OP_ORDER)
            self.state = 131
            self.match(Esgish2GrammarParser.ARG)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 132
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringListQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_STRING_LIST(self):
            return self.getToken(Esgish2GrammarParser.OP_STRING_LIST, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def OP_STRING_LIST_NO_ARG(self):
            return self.getToken(Esgish2GrammarParser.OP_STRING_LIST_NO_ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_stringListQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringListQuery" ):
                listener.enterStringListQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringListQuery" ):
                listener.exitStringListQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringListQuery" ):
                return visitor.visitStringListQuery(self)
            else:
                return visitor.visitChildren(self)




    def stringListQuery(self):

        localctx = Esgish2GrammarParser.StringListQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stringListQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(Esgish2GrammarParser.FACTOR)
                self.state = 136
                self.match(Esgish2GrammarParser.OP_STRING_LIST)
                self.state = 137
                self.match(Esgish2GrammarParser.ARG)
                pass

            elif la_ == 2:
                self.state = 138
                self.match(Esgish2GrammarParser.FACTOR)
                self.state = 139
                self.match(Esgish2GrammarParser.OP_STRING_LIST_NO_ARG)
                pass


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 142
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringMapQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_STRING_MAP(self):
            return self.getToken(Esgish2GrammarParser.OP_STRING_MAP, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_stringMapQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringMapQuery" ):
                listener.enterStringMapQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringMapQuery" ):
                listener.exitStringMapQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringMapQuery" ):
                return visitor.visitStringMapQuery(self)
            else:
                return visitor.visitChildren(self)




    def stringMapQuery(self):

        localctx = Esgish2GrammarParser.StringMapQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stringMapQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 146
            self.match(Esgish2GrammarParser.OP_STRING_MAP)
            self.state = 147
            self.match(Esgish2GrammarParser.ARG)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 148
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def OP_STRING_MATCH(self):
            return self.getToken(Esgish2GrammarParser.OP_STRING_MATCH, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def NULL_LIST(self):
            return self.getToken(Esgish2GrammarParser.NULL_LIST, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_stringQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringQuery" ):
                listener.enterStringQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringQuery" ):
                listener.exitStringQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringQuery" ):
                return visitor.visitStringQuery(self)
            else:
                return visitor.visitChildren(self)




    def stringQuery(self):

        localctx = Esgish2GrammarParser.StringQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stringQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 152
            self.match(Esgish2GrammarParser.OP_STRING_MATCH)
            self.state = 153
            self.match(Esgish2GrammarParser.ARG)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 154
                self.match(Esgish2GrammarParser.NULL_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SavedQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SAVED_SCREEN(self):
            return self.getToken(Esgish2GrammarParser.SAVED_SCREEN, 0)

        def OP_BOOLEAN(self):
            return self.getToken(Esgish2GrammarParser.OP_BOOLEAN, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_savedQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSavedQuery" ):
                listener.enterSavedQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSavedQuery" ):
                listener.exitSavedQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSavedQuery" ):
                return visitor.visitSavedQuery(self)
            else:
                return visitor.visitChildren(self)




    def savedQuery(self):

        localctx = Esgish2GrammarParser.SavedQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_savedQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(Esgish2GrammarParser.SAVED_SCREEN)
            self.state = 158
            self.match(Esgish2GrammarParser.OP_BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WrappedSavedQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def savedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SavedQueryContext,0)


        def wrappedSavedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.WrappedSavedQueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_wrappedSavedQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrappedSavedQuery" ):
                listener.enterWrappedSavedQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrappedSavedQuery" ):
                listener.exitWrappedSavedQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrappedSavedQuery" ):
                return visitor.visitWrappedSavedQuery(self)
            else:
                return visitor.visitChildren(self)




    def wrappedSavedQuery(self):

        localctx = Esgish2GrammarParser.WrappedSavedQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_wrappedSavedQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(Esgish2GrammarParser.T__0)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 161
                self.savedQuery()
                pass
            elif token in [1]:
                self.state = 162
                self.wrappedSavedQuery()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CustomScoreQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUSTOM_SCORE(self):
            return self.getToken(Esgish2GrammarParser.CUSTOM_SCORE, 0)

        def OP_ORDER(self):
            return self.getToken(Esgish2GrammarParser.OP_ORDER, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_customScoreQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCustomScoreQuery" ):
                listener.enterCustomScoreQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCustomScoreQuery" ):
                listener.exitCustomScoreQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCustomScoreQuery" ):
                return visitor.visitCustomScoreQuery(self)
            else:
                return visitor.visitChildren(self)




    def customScoreQuery(self):

        localctx = Esgish2GrammarParser.CustomScoreQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_customScoreQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(Esgish2GrammarParser.CUSTOM_SCORE)
            self.state = 168
            self.match(Esgish2GrammarParser.OP_ORDER)
            self.state = 169
            self.match(Esgish2GrammarParser.ARG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(Esgish2GrammarParser.AND, 0)

        def groupQueryElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Esgish2GrammarParser.GroupQueryElementContext)
            else:
                return self.getTypedRuleContext(Esgish2GrammarParser.GroupQueryElementContext,i)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_andQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndQuery" ):
                listener.enterAndQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndQuery" ):
                listener.exitAndQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndQuery" ):
                return visitor.visitAndQuery(self)
            else:
                return visitor.visitChildren(self)




    def andQuery(self):

        localctx = Esgish2GrammarParser.AndQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_andQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(Esgish2GrammarParser.AND)
            self.state = 172
            self.match(Esgish2GrammarParser.T__0)
            self.state = 173
            self.groupQueryElement()
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.match(Esgish2GrammarParser.T__2)
                self.state = 175
                self.groupQueryElement()
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 180
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(Esgish2GrammarParser.OR, 0)

        def groupQueryElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Esgish2GrammarParser.GroupQueryElementContext)
            else:
                return self.getTypedRuleContext(Esgish2GrammarParser.GroupQueryElementContext,i)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_orQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrQuery" ):
                listener.enterOrQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrQuery" ):
                listener.exitOrQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrQuery" ):
                return visitor.visitOrQuery(self)
            else:
                return visitor.visitChildren(self)




    def orQuery(self):

        localctx = Esgish2GrammarParser.OrQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_orQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(Esgish2GrammarParser.OR)
            self.state = 183
            self.match(Esgish2GrammarParser.T__0)
            self.state = 184
            self.groupQueryElement()
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self.match(Esgish2GrammarParser.T__2)
                self.state = 186
                self.groupQueryElement()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 191
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegatedQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(Esgish2GrammarParser.NOT, 0)

        def wrappedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.WrappedQueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_negatedQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegatedQuery" ):
                listener.enterNegatedQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegatedQuery" ):
                listener.exitNegatedQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegatedQuery" ):
                return visitor.visitNegatedQuery(self)
            else:
                return visitor.visitChildren(self)




    def negatedQuery(self):

        localctx = Esgish2GrammarParser.NegatedQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_negatedQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(Esgish2GrammarParser.NOT)
            self.state = 194
            self.wrappedQuery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupQueryElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleFactorQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SingleFactorQueryContext,0)


        def andQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.AndQueryContext,0)


        def negatedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.NegatedQueryContext,0)


        def orQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.OrQueryContext,0)


        def savedQuery(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SavedQueryContext,0)


        def formula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_groupQueryElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupQueryElement" ):
                listener.enterGroupQueryElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupQueryElement" ):
                listener.exitGroupQueryElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupQueryElement" ):
                return visitor.visitGroupQueryElement(self)
            else:
                return visitor.visitChildren(self)




    def groupQueryElement(self):

        localctx = Esgish2GrammarParser.GroupQueryElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_groupQueryElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 196
                self.singleFactorQuery()
                pass

            elif la_ == 2:
                self.state = 197
                self.andQuery()
                pass

            elif la_ == 3:
                self.state = 198
                self.negatedQuery()
                pass

            elif la_ == 4:
                self.state = 199
                self.orQuery()
                pass

            elif la_ == 5:
                self.state = 200
                self.savedQuery()
                pass

            elif la_ == 6:
                self.state = 201
                self.formula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseCountFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.CaseCountFormulaContext,0)


        def ifFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.IfFormulaContext,0)


        def personCountFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.PersonCountFormulaContext,0)


        def percentileRankFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.PercentileRankFormulaContext,0)


        def percentileRankInCategoryFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.PercentileRankInCategoryFormulaContext,0)


        def quantileFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QuantileFormulaContext,0)


        def quantileFormulaInCategoryFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QuantileFormulaInCategoryFormulaContext,0)


        def rankAscendingFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.RankAscendingFormulaContext,0)


        def rankDescendingFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.RankDescendingFormulaContext,0)


        def sumFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.SumFormulaContext,0)


        def differenceFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.DifferenceFormulaContext,0)


        def coalesceFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.CoalesceFormulaContext,0)


        def ratioFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.RatioFormulaContext,0)


        def yearsSinceFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.YearsSinceFormulaContext,0)


        def booleanFormula(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.BooleanFormulaContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = Esgish2GrammarParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 204
                self.caseCountFormula()
                pass
            elif token in [16]:
                self.state = 205
                self.ifFormula()
                pass
            elif token in [17]:
                self.state = 206
                self.personCountFormula()
                pass
            elif token in [19]:
                self.state = 207
                self.percentileRankFormula()
                pass
            elif token in [18]:
                self.state = 208
                self.percentileRankInCategoryFormula()
                pass
            elif token in [20]:
                self.state = 209
                self.quantileFormula()
                pass
            elif token in [21]:
                self.state = 210
                self.quantileFormulaInCategoryFormula()
                pass
            elif token in [22]:
                self.state = 211
                self.rankAscendingFormula()
                pass
            elif token in [23]:
                self.state = 212
                self.rankDescendingFormula()
                pass
            elif token in [24]:
                self.state = 213
                self.sumFormula()
                pass
            elif token in [25]:
                self.state = 214
                self.differenceFormula()
                pass
            elif token in [26]:
                self.state = 215
                self.coalesceFormula()
                pass
            elif token in [27]:
                self.state = 216
                self.ratioFormula()
                pass
            elif token in [28]:
                self.state = 217
                self.yearsSinceFormula()
                pass
            elif token in [29]:
                self.state = 218
                self.booleanFormula()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RatioFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RATIO(self):
            return self.getToken(Esgish2GrammarParser.RATIO, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_ratioFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRatioFormula" ):
                listener.enterRatioFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRatioFormula" ):
                listener.exitRatioFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRatioFormula" ):
                return visitor.visitRatioFormula(self)
            else:
                return visitor.visitChildren(self)




    def ratioFormula(self):

        localctx = Esgish2GrammarParser.RatioFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ratioFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(Esgish2GrammarParser.RATIO)
            self.state = 222
            self.match(Esgish2GrammarParser.T__0)
            self.state = 223
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 224
            self.match(Esgish2GrammarParser.T__2)
            self.state = 225
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 226
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoalesceFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COALESCE(self):
            return self.getToken(Esgish2GrammarParser.COALESCE, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_coalesceFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoalesceFormula" ):
                listener.enterCoalesceFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoalesceFormula" ):
                listener.exitCoalesceFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoalesceFormula" ):
                return visitor.visitCoalesceFormula(self)
            else:
                return visitor.visitChildren(self)




    def coalesceFormula(self):

        localctx = Esgish2GrammarParser.CoalesceFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_coalesceFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(Esgish2GrammarParser.COALESCE)
            self.state = 229
            self.match(Esgish2GrammarParser.T__0)
            self.state = 230
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 231
            self.match(Esgish2GrammarParser.T__2)
            self.state = 232
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 233
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseCountFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE_COUNT(self):
            return self.getToken(Esgish2GrammarParser.CASE_COUNT, 0)

        def query(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_caseCountFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseCountFormula" ):
                listener.enterCaseCountFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseCountFormula" ):
                listener.exitCaseCountFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseCountFormula" ):
                return visitor.visitCaseCountFormula(self)
            else:
                return visitor.visitChildren(self)




    def caseCountFormula(self):

        localctx = Esgish2GrammarParser.CaseCountFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_caseCountFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(Esgish2GrammarParser.CASE_COUNT)
            self.state = 236
            self.match(Esgish2GrammarParser.T__0)
            self.state = 237
            self.query()
            self.state = 238
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Esgish2GrammarParser.IF, 0)

        def ARG(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.ARG)
            else:
                return self.getToken(Esgish2GrammarParser.ARG, i)

        def NULL_LIST(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.NULL_LIST)
            else:
                return self.getToken(Esgish2GrammarParser.NULL_LIST, i)

        def singleFactorQuery(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Esgish2GrammarParser.SingleFactorQueryContext)
            else:
                return self.getTypedRuleContext(Esgish2GrammarParser.SingleFactorQueryContext,i)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_ifFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfFormula" ):
                listener.enterIfFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfFormula" ):
                listener.exitIfFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfFormula" ):
                return visitor.visitIfFormula(self)
            else:
                return visitor.visitChildren(self)




    def ifFormula(self):

        localctx = Esgish2GrammarParser.IfFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(Esgish2GrammarParser.IF)
            self.state = 241
            self.match(Esgish2GrammarParser.T__0)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.singleFactorQuery()
                self.state = 243
                self.match(Esgish2GrammarParser.T__2)
                self.state = 244
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.match(Esgish2GrammarParser.T__2)
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5368676448) != 0)):
                    break

            self.state = 251
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 252
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PersonCountFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERSON_COUNT(self):
            return self.getToken(Esgish2GrammarParser.PERSON_COUNT, 0)

        def query(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_personCountFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPersonCountFormula" ):
                listener.enterPersonCountFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPersonCountFormula" ):
                listener.exitPersonCountFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPersonCountFormula" ):
                return visitor.visitPersonCountFormula(self)
            else:
                return visitor.visitChildren(self)




    def personCountFormula(self):

        localctx = Esgish2GrammarParser.PersonCountFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_personCountFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(Esgish2GrammarParser.PERSON_COUNT)
            self.state = 255
            self.match(Esgish2GrammarParser.T__0)
            self.state = 256
            self.query()
            self.state = 257
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PercentileRankFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENTILE_RANK(self):
            return self.getToken(Esgish2GrammarParser.PERCENTILE_RANK, 0)

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_percentileRankFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPercentileRankFormula" ):
                listener.enterPercentileRankFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPercentileRankFormula" ):
                listener.exitPercentileRankFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercentileRankFormula" ):
                return visitor.visitPercentileRankFormula(self)
            else:
                return visitor.visitChildren(self)




    def percentileRankFormula(self):

        localctx = Esgish2GrammarParser.PercentileRankFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_percentileRankFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(Esgish2GrammarParser.PERCENTILE_RANK)
            self.state = 260
            self.match(Esgish2GrammarParser.T__0)
            self.state = 261
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 262
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PercentileRankInCategoryFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENTILE_RANK_IN_CATEGORY(self):
            return self.getToken(Esgish2GrammarParser.PERCENTILE_RANK_IN_CATEGORY, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_percentileRankInCategoryFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPercentileRankInCategoryFormula" ):
                listener.enterPercentileRankInCategoryFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPercentileRankInCategoryFormula" ):
                listener.exitPercentileRankInCategoryFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercentileRankInCategoryFormula" ):
                return visitor.visitPercentileRankInCategoryFormula(self)
            else:
                return visitor.visitChildren(self)




    def percentileRankInCategoryFormula(self):

        localctx = Esgish2GrammarParser.PercentileRankInCategoryFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_percentileRankInCategoryFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(Esgish2GrammarParser.PERCENTILE_RANK_IN_CATEGORY)
            self.state = 265
            self.match(Esgish2GrammarParser.T__0)
            self.state = 266
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 267
            self.match(Esgish2GrammarParser.T__2)
            self.state = 268
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 269
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantileFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANTILE(self):
            return self.getToken(Esgish2GrammarParser.QUANTILE, 0)

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_quantileFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantileFormula" ):
                listener.enterQuantileFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantileFormula" ):
                listener.exitQuantileFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantileFormula" ):
                return visitor.visitQuantileFormula(self)
            else:
                return visitor.visitChildren(self)




    def quantileFormula(self):

        localctx = Esgish2GrammarParser.QuantileFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_quantileFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(Esgish2GrammarParser.QUANTILE)
            self.state = 272
            self.match(Esgish2GrammarParser.T__0)
            self.state = 273
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 274
            self.match(Esgish2GrammarParser.T__2)
            self.state = 275
            self.match(Esgish2GrammarParser.ARG)
            self.state = 276
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantileFormulaInCategoryFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANTILE_IN_CATEGORY(self):
            return self.getToken(Esgish2GrammarParser.QUANTILE_IN_CATEGORY, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def ARG(self):
            return self.getToken(Esgish2GrammarParser.ARG, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_quantileFormulaInCategoryFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantileFormulaInCategoryFormula" ):
                listener.enterQuantileFormulaInCategoryFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantileFormulaInCategoryFormula" ):
                listener.exitQuantileFormulaInCategoryFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantileFormulaInCategoryFormula" ):
                return visitor.visitQuantileFormulaInCategoryFormula(self)
            else:
                return visitor.visitChildren(self)




    def quantileFormulaInCategoryFormula(self):

        localctx = Esgish2GrammarParser.QuantileFormulaInCategoryFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_quantileFormulaInCategoryFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(Esgish2GrammarParser.QUANTILE_IN_CATEGORY)
            self.state = 279
            self.match(Esgish2GrammarParser.T__0)
            self.state = 280
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 281
            self.match(Esgish2GrammarParser.T__2)
            self.state = 282
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 283
            self.match(Esgish2GrammarParser.T__2)
            self.state = 284
            self.match(Esgish2GrammarParser.ARG)
            self.state = 285
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RankAscendingFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANK_ASCENDING(self):
            return self.getToken(Esgish2GrammarParser.RANK_ASCENDING, 0)

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_rankAscendingFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRankAscendingFormula" ):
                listener.enterRankAscendingFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRankAscendingFormula" ):
                listener.exitRankAscendingFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRankAscendingFormula" ):
                return visitor.visitRankAscendingFormula(self)
            else:
                return visitor.visitChildren(self)




    def rankAscendingFormula(self):

        localctx = Esgish2GrammarParser.RankAscendingFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_rankAscendingFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(Esgish2GrammarParser.RANK_ASCENDING)
            self.state = 288
            self.match(Esgish2GrammarParser.T__0)
            self.state = 289
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 290
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RankDescendingFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANK_DESCENDING(self):
            return self.getToken(Esgish2GrammarParser.RANK_DESCENDING, 0)

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_rankDescendingFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRankDescendingFormula" ):
                listener.enterRankDescendingFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRankDescendingFormula" ):
                listener.exitRankDescendingFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRankDescendingFormula" ):
                return visitor.visitRankDescendingFormula(self)
            else:
                return visitor.visitChildren(self)




    def rankDescendingFormula(self):

        localctx = Esgish2GrammarParser.RankDescendingFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_rankDescendingFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(Esgish2GrammarParser.RANK_DESCENDING)
            self.state = 293
            self.match(Esgish2GrammarParser.T__0)
            self.state = 294
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 295
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUM(self):
            return self.getToken(Esgish2GrammarParser.SUM, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_sumFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumFormula" ):
                listener.enterSumFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumFormula" ):
                listener.exitSumFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumFormula" ):
                return visitor.visitSumFormula(self)
            else:
                return visitor.visitChildren(self)




    def sumFormula(self):

        localctx = Esgish2GrammarParser.SumFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_sumFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(Esgish2GrammarParser.SUM)
            self.state = 298
            self.match(Esgish2GrammarParser.T__0)
            self.state = 299
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 300
                self.match(Esgish2GrammarParser.T__2)
                self.state = 301
                self.match(Esgish2GrammarParser.FACTOR)
                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 306
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DifferenceFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIFFERENCE(self):
            return self.getToken(Esgish2GrammarParser.DIFFERENCE, 0)

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(Esgish2GrammarParser.FACTOR)
            else:
                return self.getToken(Esgish2GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_differenceFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifferenceFormula" ):
                listener.enterDifferenceFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifferenceFormula" ):
                listener.exitDifferenceFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifferenceFormula" ):
                return visitor.visitDifferenceFormula(self)
            else:
                return visitor.visitChildren(self)




    def differenceFormula(self):

        localctx = Esgish2GrammarParser.DifferenceFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_differenceFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(Esgish2GrammarParser.DIFFERENCE)
            self.state = 309
            self.match(Esgish2GrammarParser.T__0)
            self.state = 310
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 313 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 311
                self.match(Esgish2GrammarParser.T__2)
                self.state = 312
                self.match(Esgish2GrammarParser.FACTOR)
                self.state = 315 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 317
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YearsSinceFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YEARS_SINCE(self):
            return self.getToken(Esgish2GrammarParser.YEARS_SINCE, 0)

        def FACTOR(self):
            return self.getToken(Esgish2GrammarParser.FACTOR, 0)

        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_yearsSinceFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYearsSinceFormula" ):
                listener.enterYearsSinceFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYearsSinceFormula" ):
                listener.exitYearsSinceFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYearsSinceFormula" ):
                return visitor.visitYearsSinceFormula(self)
            else:
                return visitor.visitChildren(self)




    def yearsSinceFormula(self):

        localctx = Esgish2GrammarParser.YearsSinceFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_yearsSinceFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(Esgish2GrammarParser.YEARS_SINCE)
            self.state = 320
            self.match(Esgish2GrammarParser.T__0)
            self.state = 321
            self.match(Esgish2GrammarParser.FACTOR)
            self.state = 322
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(Esgish2GrammarParser.BOOLEAN, 0)

        def query(self):
            return self.getTypedRuleContext(Esgish2GrammarParser.QueryContext,0)


        def getRuleIndex(self):
            return Esgish2GrammarParser.RULE_booleanFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanFormula" ):
                listener.enterBooleanFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanFormula" ):
                listener.exitBooleanFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanFormula" ):
                return visitor.visitBooleanFormula(self)
            else:
                return visitor.visitChildren(self)




    def booleanFormula(self):

        localctx = Esgish2GrammarParser.BooleanFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_booleanFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(Esgish2GrammarParser.BOOLEAN)
            self.state = 325
            self.match(Esgish2GrammarParser.T__0)
            self.state = 326
            self.query()
            self.state = 327
            self.match(Esgish2GrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





