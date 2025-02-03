from Esgish2GrammarVisitor import Esgish2GrammarVisitor
from antlr4 import InputStream, CommonTokenStream
from Esgish2GrammarLexer import Esgish2GrammarLexer
from Esgish2GrammarParser import Esgish2GrammarParser

class QueryToEnglish(Esgish2GrammarVisitor):
    def visitQuery(self, ctx: Esgish2GrammarParser.QueryContext):
        """Visit different query types and return English translation."""
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
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(child, Esgish2GrammarParser.GroupQueryElementContext)]
        elements = [e for e in elements if e is not None]
        
        return " and ".join(elements)

    def visitOrQuery(self, ctx: Esgish2GrammarParser.OrQueryContext):
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(child, Esgish2GrammarParser.GroupQueryElementContext)]
        elements = [e for e in elements if e is not None]
        
        return " or ".join(elements)

    def visitGroupQueryElement(self, ctx: Esgish2GrammarParser.GroupQueryElementContext):
        return self.visit(ctx.getChild(0))

    def visitSingleFactorQuery(self, ctx: Esgish2GrammarParser.SingleFactorQueryContext):
        return self.visit(ctx.getChild(0))

    def visitNumberOrStringQuery(self, ctx: Esgish2GrammarParser.NumberOrStringQueryContext):
        factor = ctx.FACTOR().getText().replace('[', '').replace(']', '')  
        operator = ctx.OP_ORDER().getText()
        argument = ctx.ARG().getText().replace("'", "") if ctx.ARG() else "Unknown value"
        ##factor = factor.replace('[', '').replace(']', '')  

        operator_mapping = {
            "<=": "is less than or equal to",
            ">=": "is greater than or equal to",
            "<": "is less than",
            ">": "is greater than",
            "==": "is equal to"
        }
        
        english_operator = operator_mapping.get(operator, "has an unknown relation to")
        
        return f"{factor} {english_operator} {argument}"

query = "AND([CannabisRevShareMax] == '5', AND([CannabisRevShareMax] >= '1',  [CarbonRRPerformanceScore] > '3'))"
input_stream = InputStream(query)
lexer = Esgish2GrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Esgish2GrammarParser(token_stream)
tree = parser.query()

translator = QueryToEnglish()

print("Translated Query: ", translator.visit(tree))
