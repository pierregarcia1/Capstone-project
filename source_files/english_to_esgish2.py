import re
from Esgish2GrammarVisitor import Esgish2GrammarVisitor
from antlr4 import InputStream, CommonTokenStream
from Esgish2GrammarLexer import Esgish2GrammarLexer
from Esgish2GrammarParser import Esgish2GrammarParser

class EnglishToQuery:
    def visitAndQuery(self, english_query):
        # Translate "X and Y" to "AND(X, Y)"
        parts = re.split(r'\s+and\s+(?=[a-zA-Z0-9_]+\s+is\s+)', english_query)
        
        # If no valid split occurs, process as a single comparison
        if len(parts) == 1:
            return self.visitComparisonQuery(english_query)  # Directly process if it's a single condition
        
        # Convert each part into ESGish2 format
        esgish_parts = [self.visitComparisonQuery(part.strip()) for part in parts]
        return f"AND({', '.join(esgish_parts)})"

    def visitOrQuery(self, english_query):
        # Translate "X or Y" to "OR(X, Y)"
        # Split only when 'or' is separating full conditions (e.g., "X is Y or Z is W")
        parts = re.split(r'\s+or\s+(?=[a-zA-Z0-9_]+\s+is\s+)', english_query)
        
        # If no valid split occurs, process as a single comparison
        if len(parts) == 1:
            return self.visitComparisonQuery(english_query)  # Directly process if it's a single condition
        
        # Convert each part into ESGish2 format
        esgish_parts = [self.visitComparisonQuery(part.strip()) for part in parts]
        return f"OR({', '.join(esgish_parts)})"

    def visitComparisonQuery(self, english_query):
        # Handles comparison like 'X is greater than or equal to Y'.
        # Extracts the factor (variable) and comparison statement
        parts = re.match(r'(.+?) is (.+)', english_query)
        if not parts:
            return "Invalid query format"
        
        factor = parts.group(1).strip()  # Extract factor
        comparison = parts.group(2).strip() # Extract full comparison phrase
        # Debugging output
        # print("DEBUG: Factor =", factor)
        # print("DEBUG: Comparison =", comparison)

        # Mapping of English phrases to ESGish2 operators
        operator_mapping = {
            "less than or equal to": "<=",
            "greater than or equal to": ">=",
            "not equal to": "!=",
            "less than": "<",
            "greater than": ">",
            "equal to": "==",
            "contains any of": "ANY",
            "contains none of": "NONE",
            "contains all of": "ALL",
            "is in": "IN",
            "contains": "CTN",
            "loosely contains": "LCTN",
            "starts with": "STW"
        }
        # Ensure the longest matches are checked first to avoid partial matches
        for phrase in sorted(operator_mapping.keys(), key=len, reverse=True):  # Sort by length (longest first)
            if comparison.startswith(phrase):
                argument = comparison[len(phrase):].strip().strip("'") # Extract the numerical value
                
                # Handle missing values
                if not argument:
                    return f"Error: Missing value after '{phrase}' in query '{english_query}'"
                
                 # **Handle numeric values separately**
                if operator_mapping[phrase] not in {"ANY", "NONE", "ALL", "IN", "CTN", "LCTN", "STW"}:
                    if not re.match(r'^-?\d+(\.\d+)?$', argument):  # Validate as a number
                        return f"Error: Invalid number format '{argument}' in query '{english_query}'"
                    
                # Convert to ESGish2 format
                return f"[{factor}] {operator_mapping[phrase]} '{argument}'"
        return "Invalid operator"

    def visit(self, english_query):
        # Prevents infinite recursion by checking if the query is already a comparison statement
        # Base case: If the query is a simple comparison without 'and'/'or', process directly
        if " is " in english_query and not (" and " in english_query or " or " in english_query):
            return self.visitComparisonQuery(english_query)

        # If 'and' or 'or' exists, call the corresponding processing function
        if ' and ' in english_query:
            return self.visitAndQuery(english_query)
        elif ' or ' in english_query:
            return self.visitOrQuery(english_query)
        
        return "Invalid query format"

# Example English query
# english_query = "CannabisRevShareMax is less than or equal to 5 and CannabisRevShareMax is less than or equal to 1 and CarbonRRPerformanceScore is equal to 3"
# translator = EnglishToQuery()
# esgish_query = translator.visit(english_query)
# print("ESGish2 Query: ", esgish_query)

queries = [
    "CannabisRevShareMax is less than or equal to 5 and CannabisRevShareMax is less than or equal to 1 and CarbonRRPerformanceScore is equal to 3",  # Example English query
    "Sector is in 'Finance|Technology|Healthcare'",  # String-based IN
    "CompanyName contains 'Apple'",                 # String-based CTN
    "Industry loosely contains 'tech'",             # String-based LCTN
    "Ticker starts with 'AAPL'",                    # String-based STW
    "Revenue is greater than 1000",                 # Numeric comparison
    "MarketCap is less than or equal to 500000",    # Numeric comparison
    "RiskCategory contains any of 'High|Medium'",   # String-based ANY
    "ESGScore contains none of 'Low|Very Low'",     # String-based NONE
    "ClimatePolicy contains all of 'CarbonNeutral|NetZero'"  # String-based ALL
]

translator = EnglishToQuery()

for q in queries:
    print(f"English: {q}")
    print(f"ESGish2: {translator.visit(q)}\n")