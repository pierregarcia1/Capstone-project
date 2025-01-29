from source_files import QueryParser
from QueryVisitor import QueryVisitor

class QueryToEnglish(QueryVisitor):
    def visitQuery(self, ctx: QueryParser.QueryContext):
        columns = self.visit(ctx.columns())
        table = ctx.table().getText()
        condition = self.visit(ctx.condition())
        return f"Retrieve {columns} from the {table} table where {condition}."

    def visitColumns(self, ctx: QueryParser.ColumnsContext):
        return ', '.join([col.getText() for col in ctx.IDENTIFIER()])

    def visitCondition(self, ctx: QueryParser.ConditionContext):
        column = ctx.IDENTIFIER().getText()
        operator = ctx.OPERATOR().getText()
        value = ctx.value().getText()

        op_translation = {
            '=': "is equal to",
            '>': "is greater than",
            '<': "is less than",
            '>=': "is greater than or equal to",
            '<=': "is less than or equal to",
        }
        return f"{column} {op_translation[operator]} {value}"

# Example usage
from antlr4 import InputStream, CommonTokenStream
from QueryLexer import QueryLexer
from QueryParser import QueryParser

query = "SELECT name, age FROM users WHERE age > 30;"
input_stream = InputStream(query)
lexer = QueryLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = QueryParser(token_stream)
tree = parser.query()

translator = QueryToEnglish()
print(translator.visit(tree))  # Output: "Retrieve name, age from the users table where age is greater than 30."
