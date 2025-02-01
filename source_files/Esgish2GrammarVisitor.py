# Generated from Esgish2Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Esgish2GrammarParser import Esgish2GrammarParser
else:
    from Esgish2GrammarParser import Esgish2GrammarParser

# This class defines a complete generic visitor for a parse tree produced by Esgish2GrammarParser.

class Esgish2GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Esgish2GrammarParser#start.
    def visitStart(self, ctx:Esgish2GrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#query.
    def visitQuery(self, ctx:Esgish2GrammarParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#wrappedQuery.
    def visitWrappedQuery(self, ctx:Esgish2GrammarParser.WrappedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#singleFactorQuery.
    def visitSingleFactorQuery(self, ctx:Esgish2GrammarParser.SingleFactorQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#booleanQuery.
    def visitBooleanQuery(self, ctx:Esgish2GrammarParser.BooleanQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#dateQuery.
    def visitDateQuery(self, ctx:Esgish2GrammarParser.DateQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#formulaQuery.
    def visitFormulaQuery(self, ctx:Esgish2GrammarParser.FormulaQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#nullTypeQuery.
    def visitNullTypeQuery(self, ctx:Esgish2GrammarParser.NullTypeQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#numberOrStringQuery.
    def visitNumberOrStringQuery(self, ctx:Esgish2GrammarParser.NumberOrStringQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#stringListQuery.
    def visitStringListQuery(self, ctx:Esgish2GrammarParser.StringListQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#stringMapQuery.
    def visitStringMapQuery(self, ctx:Esgish2GrammarParser.StringMapQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#stringQuery.
    def visitStringQuery(self, ctx:Esgish2GrammarParser.StringQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#savedQuery.
    def visitSavedQuery(self, ctx:Esgish2GrammarParser.SavedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#wrappedSavedQuery.
    def visitWrappedSavedQuery(self, ctx:Esgish2GrammarParser.WrappedSavedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#customScoreQuery.
    def visitCustomScoreQuery(self, ctx:Esgish2GrammarParser.CustomScoreQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#andQuery.
    def visitAndQuery(self, ctx:Esgish2GrammarParser.AndQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#orQuery.
    def visitOrQuery(self, ctx:Esgish2GrammarParser.OrQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#negatedQuery.
    def visitNegatedQuery(self, ctx:Esgish2GrammarParser.NegatedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#groupQueryElement.
    def visitGroupQueryElement(self, ctx:Esgish2GrammarParser.GroupQueryElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#formula.
    def visitFormula(self, ctx:Esgish2GrammarParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#ratioFormula.
    def visitRatioFormula(self, ctx:Esgish2GrammarParser.RatioFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#coalesceFormula.
    def visitCoalesceFormula(self, ctx:Esgish2GrammarParser.CoalesceFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#caseCountFormula.
    def visitCaseCountFormula(self, ctx:Esgish2GrammarParser.CaseCountFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#ifFormula.
    def visitIfFormula(self, ctx:Esgish2GrammarParser.IfFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#personCountFormula.
    def visitPersonCountFormula(self, ctx:Esgish2GrammarParser.PersonCountFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#percentileRankFormula.
    def visitPercentileRankFormula(self, ctx:Esgish2GrammarParser.PercentileRankFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#percentileRankInCategoryFormula.
    def visitPercentileRankInCategoryFormula(self, ctx:Esgish2GrammarParser.PercentileRankInCategoryFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#quantileFormula.
    def visitQuantileFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#quantileFormulaInCategoryFormula.
    def visitQuantileFormulaInCategoryFormula(self, ctx:Esgish2GrammarParser.QuantileFormulaInCategoryFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#rankAscendingFormula.
    def visitRankAscendingFormula(self, ctx:Esgish2GrammarParser.RankAscendingFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#rankDescendingFormula.
    def visitRankDescendingFormula(self, ctx:Esgish2GrammarParser.RankDescendingFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#sumFormula.
    def visitSumFormula(self, ctx:Esgish2GrammarParser.SumFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#differenceFormula.
    def visitDifferenceFormula(self, ctx:Esgish2GrammarParser.DifferenceFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#yearsSinceFormula.
    def visitYearsSinceFormula(self, ctx:Esgish2GrammarParser.YearsSinceFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Esgish2GrammarParser#booleanFormula.
    def visitBooleanFormula(self, ctx:Esgish2GrammarParser.BooleanFormulaContext):
        return self.visitChildren(ctx)



del Esgish2GrammarParser