import re
from Esgish2GrammarVisitor import Esgish2GrammarVisitor
from antlr4 import InputStream, CommonTokenStream
from Esgish2GrammarLexer import Esgish2GrammarLexer
from Esgish2GrammarParser import Esgish2GrammarParser

class EnglishToQuery:
    def visitAndQuery(self, english_query):
        # Translate "X and Y" to "AND(X, Y)"
        parts = english_query.split(' and ')
        esgish_parts = [self.visit(part.strip()) for part in parts]
        return f"AND({', '.join(esgish_parts)})"

    def visitOrQuery(self, english_query):
        # Translate "X or Y" to "OR(X, Y)"
        parts = english_query.split(' or ')
        esgish_parts = [self.visit(part.strip()) for part in parts]
        return f"OR({', '.join(esgish_parts)})"

    def visitComparisonQuery(self, english_query):
        parts = english_query.split(' is ')
        if len(parts) != 2:
            return "Invalid query format"
        
        factor = parts[0].strip()
        comparison = parts[1].strip()

        # Determine the operator and argument based on simple string comparison
        if "less than" in comparison:
            argument = comparison.replace("less than", "").strip()
            return f"[{factor}] < '{argument}'"
        elif "greater than" in comparison:
            argument = comparison.replace("greater than", "").strip()
            return f"[{factor}] > '{argument}'"
        elif "equal to" in comparison:
            argument = comparison.replace("equal to", "").strip()
            return f"[{factor}] = '{argument}'"
        else:
            return "Invalid operator"

    def visit(self, english_query):
        # Main entry point for translation from English to ESGish2
        if ' and ' in english_query:
            return self.visitAndQuery(english_query)
        elif ' or ' in english_query:
            return self.visitOrQuery(english_query)
        else:
            return self.visitComparisonQuery(english_query)


# Example English query
english_query = "CannabisRevShareMax is less than 5 and CannabisRevShareMax is less than 1 and CarbonRRPerformanceScore is greater than 3"
translator = EnglishToQuery()
esgish_query = translator.visit(english_query)
print("ESGish2 Query: ", esgish_query)
