from Esgish2GrammarVisitor import Esgish2GrammarVisitor
from antlr4 import InputStream, CommonTokenStream
from Esgish2GrammarLexer import Esgish2GrammarLexer
from Esgish2GrammarParser import Esgish2GrammarParser


class QueryToEnglish(Esgish2GrammarVisitor):
    def visitQuery(self, ctx: Esgish2GrammarParser.QueryContext):
        if ctx.singleFactorQuery():
            return self.visit(ctx.singleFactorQuery())
        elif ctx.andQuery():
            return self.visit(ctx.andQuery())
        elif ctx.orQuery():
            return self.visit(ctx.orQuery())
        elif ctx.negatedQuery():
            return self.visit(ctx.negatedQuery())
        elif ctx.savedQuery():
            return self.visit(ctx.savedQuery())
        elif ctx.customScoreQuery():
            return self.visit(ctx.customScoreQuery())
        else:
            return "Invalid query."

    def visitAndQuery(self, ctx: Esgish2GrammarParser.AndQueryContext):
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(
            child, Esgish2GrammarParser.GroupQueryElementContext)]
        elements = [e for e in elements if e is not None]

        return " and ".join(elements)

    def visitOrQuery(self, ctx: Esgish2GrammarParser.OrQueryContext):
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(
            child, Esgish2GrammarParser.GroupQueryElementContext)]
        elements = [e for e in elements if e is not None]

        return " or ".join(elements)

    def visitGroupQueryElement(self, ctx: Esgish2GrammarParser.GroupQueryElementContext):
        return self.visit(ctx.getChild(0))

    def visitSingleFactorQuery(self, ctx: Esgish2GrammarParser.SingleFactorQueryContext):
        return self.visit(ctx.getChild(0))

    def visitNumberOrStringQuery(self, ctx: Esgish2GrammarParser.NumberOrStringQueryContext):
        factor = ctx.FACTOR().getText()

        operator = ctx.getText()

        if '<' in operator:
            operator = "is less than"
        elif '>' in operator:
            operator = "is greater than"
        elif '=' in operator:
            operator = "is equal to"
        else:
            operator = "Unknown operator"

        argument = ctx.ARG().getText() if ctx.ARG() else "Unknown value"

        return f"{factor} {operator} {argument}"


query = "AND([CannabisRevShareMax] < '1', AND([CannabisRevShareMax] < '1',  [CarbonRRPerformanceScore] > '3'))"
input_stream = InputStream(query)
lexer = Esgish2GrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Esgish2GrammarParser(token_stream)
tree = parser.query()

translator = QueryToEnglish()

print("Translated Query: ", translator.visit(tree))
