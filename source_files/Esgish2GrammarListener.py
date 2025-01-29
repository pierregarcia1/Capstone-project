# Generated from Esgish2Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Esgish2GrammarParser import Esgish2GrammarParser
else:
    from Esgish2GrammarParser import Esgish2GrammarParser

# This class defines a complete listener for a parse tree produced by Esgish2GrammarParser.
class Esgish2GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by Esgish2GrammarParser#start.
    def enterStart(self, ctx:Esgish2GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#start.
    def exitStart(self, ctx:Esgish2GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#query.
    def enterQuery(self, ctx:Esgish2GrammarParser.QueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#query.
    def exitQuery(self, ctx:Esgish2GrammarParser.QueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#wrappedQuery.
    def enterWrappedQuery(self, ctx:Esgish2GrammarParser.WrappedQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#wrappedQuery.
    def exitWrappedQuery(self, ctx:Esgish2GrammarParser.WrappedQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#singleFactorQuery.
    def enterSingleFactorQuery(self, ctx:Esgish2GrammarParser.SingleFactorQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#singleFactorQuery.
    def exitSingleFactorQuery(self, ctx:Esgish2GrammarParser.SingleFactorQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#booleanQuery.
    def enterBooleanQuery(self, ctx:Esgish2GrammarParser.BooleanQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#booleanQuery.
    def exitBooleanQuery(self, ctx:Esgish2GrammarParser.BooleanQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#dateQuery.
    def enterDateQuery(self, ctx:Esgish2GrammarParser.DateQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#dateQuery.
    def exitDateQuery(self, ctx:Esgish2GrammarParser.DateQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#formulaQuery.
    def enterFormulaQuery(self, ctx:Esgish2GrammarParser.FormulaQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#formulaQuery.
    def exitFormulaQuery(self, ctx:Esgish2GrammarParser.FormulaQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#nullTypeQuery.
    def enterNullTypeQuery(self, ctx:Esgish2GrammarParser.NullTypeQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#nullTypeQuery.
    def exitNullTypeQuery(self, ctx:Esgish2GrammarParser.NullTypeQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#numberOrStringQuery.
    def enterNumberOrStringQuery(self, ctx:Esgish2GrammarParser.NumberOrStringQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#numberOrStringQuery.
    def exitNumberOrStringQuery(self, ctx:Esgish2GrammarParser.NumberOrStringQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#stringListQuery.
    def enterStringListQuery(self, ctx:Esgish2GrammarParser.StringListQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#stringListQuery.
    def exitStringListQuery(self, ctx:Esgish2GrammarParser.StringListQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#stringMapQuery.
    def enterStringMapQuery(self, ctx:Esgish2GrammarParser.StringMapQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#stringMapQuery.
    def exitStringMapQuery(self, ctx:Esgish2GrammarParser.StringMapQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#stringQuery.
    def enterStringQuery(self, ctx:Esgish2GrammarParser.StringQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#stringQuery.
    def exitStringQuery(self, ctx:Esgish2GrammarParser.StringQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#savedQuery.
    def enterSavedQuery(self, ctx:Esgish2GrammarParser.SavedQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#savedQuery.
    def exitSavedQuery(self, ctx:Esgish2GrammarParser.SavedQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#wrappedSavedQuery.
    def enterWrappedSavedQuery(self, ctx:Esgish2GrammarParser.WrappedSavedQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#wrappedSavedQuery.
    def exitWrappedSavedQuery(self, ctx:Esgish2GrammarParser.WrappedSavedQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#customScoreQuery.
    def enterCustomScoreQuery(self, ctx:Esgish2GrammarParser.CustomScoreQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#customScoreQuery.
    def exitCustomScoreQuery(self, ctx:Esgish2GrammarParser.CustomScoreQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#andQuery.
    def enterAndQuery(self, ctx:Esgish2GrammarParser.AndQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#andQuery.
    def exitAndQuery(self, ctx:Esgish2GrammarParser.AndQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#orQuery.
    def enterOrQuery(self, ctx:Esgish2GrammarParser.OrQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#orQuery.
    def exitOrQuery(self, ctx:Esgish2GrammarParser.OrQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#negatedQuery.
    def enterNegatedQuery(self, ctx:Esgish2GrammarParser.NegatedQueryContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#negatedQuery.
    def exitNegatedQuery(self, ctx:Esgish2GrammarParser.NegatedQueryContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#groupQueryElement.
    def enterGroupQueryElement(self, ctx:Esgish2GrammarParser.GroupQueryElementContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#groupQueryElement.
    def exitGroupQueryElement(self, ctx:Esgish2GrammarParser.GroupQueryElementContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#formula.
    def enterFormula(self, ctx:Esgish2GrammarParser.FormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#formula.
    def exitFormula(self, ctx:Esgish2GrammarParser.FormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#ratioFormula.
    def enterRatioFormula(self, ctx:Esgish2GrammarParser.RatioFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#ratioFormula.
    def exitRatioFormula(self, ctx:Esgish2GrammarParser.RatioFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#coalesceFormula.
    def enterCoalesceFormula(self, ctx:Esgish2GrammarParser.CoalesceFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#coalesceFormula.
    def exitCoalesceFormula(self, ctx:Esgish2GrammarParser.CoalesceFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#caseCountFormula.
    def enterCaseCountFormula(self, ctx:Esgish2GrammarParser.CaseCountFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#caseCountFormula.
    def exitCaseCountFormula(self, ctx:Esgish2GrammarParser.CaseCountFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#ifFormula.
    def enterIfFormula(self, ctx:Esgish2GrammarParser.IfFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#ifFormula.
    def exitIfFormula(self, ctx:Esgish2GrammarParser.IfFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#personCountFormula.
    def enterPersonCountFormula(self, ctx:Esgish2GrammarParser.PersonCountFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#personCountFormula.
    def exitPersonCountFormula(self, ctx:Esgish2GrammarParser.PersonCountFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#percentileRankFormula.
    def enterPercentileRankFormula(self, ctx:Esgish2GrammarParser.PercentileRankFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#percentileRankFormula.
    def exitPercentileRankFormula(self, ctx:Esgish2GrammarParser.PercentileRankFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#percentileRankInCategoryFormula.
    def enterPercentileRankInCategoryFormula(self, ctx:Esgish2GrammarParser.PercentileRankInCategoryFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#percentileRankInCategoryFormula.
    def exitPercentileRankInCategoryFormula(self, ctx:Esgish2GrammarParser.PercentileRankInCategoryFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#quantileFormula.
    def enterQuantileFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#quantileFormula.
    def exitQuantileFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#quantileFormulaInCategoryFormula.
    def enterQuantileFormulaInCategoryFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaInCategoryFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#quantileFormulaInCategoryFormula.
    def exitQuantileFormulaInCategoryFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaInCategoryFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#rankAscendingFormula.
    def enterRankAscendingFormula(self, ctx:Esgish2GrammarParser.RankAscendingFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#rankAscendingFormula.
    def exitRankAscendingFormula(self, ctx:Esgish2GrammarParser.RankAscendingFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#rankDescendingFormula.
    def enterRankDescendingFormula(self, ctx:Esgish2GrammarParser.RankDescendingFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#rankDescendingFormula.
    def exitRankDescendingFormula(self, ctx:Esgish2GrammarParser.RankDescendingFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#sumFormula.
    def enterSumFormula(self, ctx:Esgish2GrammarParser.SumFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#sumFormula.
    def exitSumFormula(self, ctx:Esgish2GrammarParser.SumFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#differenceFormula.
    def enterDifferenceFormula(self, ctx:Esgish2GrammarParser.DifferenceFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#differenceFormula.
    def exitDifferenceFormula(self, ctx:Esgish2GrammarParser.DifferenceFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#yearsSinceFormula.
    def enterYearsSinceFormula(self, ctx:Esgish2GrammarParser.YearsSinceFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#yearsSinceFormula.
    def exitYearsSinceFormula(self, ctx:Esgish2GrammarParser.YearsSinceFormulaContext):
        pass


    # Enter a parse tree produced by Esgish2GrammarParser#booleanFormula.
    def enterBooleanFormula(self, ctx:Esgish2GrammarParser.BooleanFormulaContext):
        pass

    # Exit a parse tree produced by Esgish2GrammarParser#booleanFormula.
    def exitBooleanFormula(self, ctx:Esgish2GrammarParser.BooleanFormulaContext):
        pass



del Esgish2GrammarParser