from Esgish2GrammarVisitor import Esgish2GrammarVisitor
from antlr4 import InputStream, CommonTokenStream
from Esgish2GrammarLexer import Esgish2GrammarLexer
from Esgish2GrammarParser import Esgish2GrammarParser

def is_integer(s):
    return s.lstrip('-').isdigit()

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_string(s):
    return not (is_integer(s) or is_float(s))

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
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(child, Esgish2GrammarParser.GroupQueryElementContext)]
        return " and ".join(filter(None, elements))

    def visitOrQuery(self, ctx: Esgish2GrammarParser.OrQueryContext):
        elements = [self.visit(child) for child in ctx.getChildren() if isinstance(child, Esgish2GrammarParser.GroupQueryElementContext)]
        return " or ".join(filter(None, elements))

    def visitGroupQueryElement(self, ctx: Esgish2GrammarParser.GroupQueryElementContext):
        return self.visit(ctx.getChild(0))

    def visitSingleFactorQuery(self, ctx: Esgish2GrammarParser.SingleFactorQueryContext):
        return self.visit(ctx.getChild(0))

    def visitNumberOrStringQuery(self, ctx: Esgish2GrammarParser.NumberOrStringQueryContext):
        factor = ctx.FACTOR().getText().strip('[]')
        operator = ctx.OP_ORDER().getText()
        argument = ctx.ARG().getText().strip("'") if ctx.ARG() else "Unknown value"
        
        operator_mapping = {
            "<=": "is less than or equal to",
            ">=": "is greater than or equal to",
            "<": "is less than",
            ">": "is greater than",
            "==": "is equal to",
            "!=": "is not equal to"
        }
        
        english_operator = operator_mapping.get(operator, "has an unknown relation to")

        if is_string(argument):
            if english_operator == 'is equal to':
                english_operator = "is"
            elif english_operator == 'is not equal to':
                english_operator = "is not"
    
        return f"{factor} {english_operator} {argument}"

    def visitSavedQuery(self, ctx: Esgish2GrammarParser.SavedQueryContext):
        screen = ctx.SAVED_SCREEN().getText().strip('[]')
        return f"Using saved query from {screen}"
    
    def visitCustomScoreQuery(self, ctx: Esgish2GrammarParser.CustomScoreQueryContext):
        score = ctx.CUSTOM_SCORE().getText().strip('[]')
        return f"Custom scoring query with ID {score}"
    
    def visitBooleanQuery(self, ctx: Esgish2GrammarParser.BooleanQueryContext):
        factor = ctx.FACTOR().getText().strip('[]') if ctx.FACTOR() else "Condition"
        boolean_value = ctx.OP_BOOLEAN().getText()
        return f"{factor} is {boolean_value.lower()}"

    def visitNullTypeQuery(self, ctx: Esgish2GrammarParser.NullTypeQueryContext):
        #print("DEBUG: Entered visitNullTypeQuery")
        factor = ctx.FACTOR().getText().strip('[]')
        #print(f"DEBUG: Factor = {factor}")
        return f"{factor} is null"
    
    def visitStringQuery(self, ctx: Esgish2GrammarParser.StringQueryContext): # visitStringQuery
        factor = ctx.FACTOR().getText().strip('[]')
        operator = ctx.OP_STRING_MATCH().getText()
        argument = ctx.ARG().getText().strip("'")
        
        match_mapping = {
            "CTN": "contains",
            "LCTN": "loosely contains",
            "STW": "starts with"
        }
        
        english_operator = match_mapping.get(operator, "matches")
        return f"{factor} {english_operator} '{argument}'"
    
    def visitStringListQuery(self, ctx: Esgish2GrammarParser.StringListQueryContext):
        factor = ctx.FACTOR().getText().strip('[]')
        operator = ctx.OP_STRING_LIST().getText()
        argument = ctx.ARG().getText().strip("'")
        
        list_mapping = {
            "ANY": "contains any of",
            "NONE": "contains none of",
            "ALL": "contains all of",
            "IN": "is in"
        }
        
        english_operator = list_mapping.get(operator, "relates to")

        return f"{factor} {english_operator} '{argument}'"
    

    #def visitStringListNoArgQuery(self, ctx: Esgish2GrammarParser.StringListQueryContext):
    #    factor = ctx.FACTOR().getText().strip('[]')
    #    return f"{factor} is empty"
    
    def visitStringMapQuery(self, ctx: Esgish2GrammarParser.StringMapQueryContext):
        factor = ctx.FACTOR().getText().strip('[]')
        return f"{factor} has any mapping"
    
    def visitDateQuery(self, ctx: Esgish2GrammarParser.DateQueryContext):
        factor = ctx.FACTOR().getText().strip('[]')
        operator = ctx.OP_DATE().getText()
        date_value = ctx.ARG().getText().strip("'") if ctx.ARG() else "an unknown date"

        
        date_mapping = {
            "PRE": "is before",
            "PST": "is after"
        }
        
        english_operator = date_mapping.get(operator, "has a date relation to")
        return f"{factor} {english_operator} {date_value}"


query = "OR([OilSandsRevShareMin] >= '0.5',[CivFARevShareInterval] IN '[10-15%)|[15-20%)|[20-25%)|[25-50%)|[50-100%]',[TobaccoRevShareInterval] IN '[10-15%)|[15-20%)|[20-25%)|[25-50%)|[50-100%]',[GamblingRevShareInterval] IN '[10-15%)|[15-20%)|[20-25%)|[25-50%)|[50-100%]',[CoalMiningRevShareMinThermal] >= '0.5')" # "AND([CannabisRevShareMax] <= '5', AND([CannabisRevShareMax] >= '1',  [CarbonRRPerformanceScore] > '3'))"

in_query = "[CaseAreas] IN 'Global Sanctions>Iran'"             # Q 286 Query 286 in the document (still containing null queries at the beginning)
greater_query = "[caseID] > '0'"                                # Q 313
contains_query = "[CaseProfileNote] CTN 'lithium'"              # Q 315 
boolean_query = "[BrownExpInvolved] True"                       # Q 230
date_query = "[ClimateGHGEmissionsLastUpdate] PRE '2024-06-25'" # Q 471 
null_query = "[CCACorruptionPerceptionIndex] null '44'"         # Q 383 --- ERROR

range_query = "[CivFARevShareInterval] IN '[1-5%)|[5-10%)|[10-15%)|[15-20%)|[20-25%)|[25-50%)|[50-100%]'" # Q 429 --- Bad conversion due to lack of understanding
range2_query = "[ESGFRating] IN 'A+|A|A-|B+|B|B-|C+|C|C-|D+|D|D-'"  # Q 919

string_equals_query = "[ClimateGHGReductionTargets] == 'No Target'" # Q 474
number_equals_query = "[ClimateGHGReductionTargets] == '1.5'"       # Q 474 edited


# input_stream = InputStream(range2_query)
# lexer = Esgish2GrammarLexer(input_stream)
# token_stream = CommonTokenStream(lexer)
# parser = Esgish2GrammarParser(token_stream)
# tree = parser.query()

# translator = QueryToEnglish()

# print("Translated Query: ", translator.visit(tree))

queries = {
    "OR Query": query,
    "IN Query": in_query,
    "Greater Than Query": greater_query,
    "Contains Query": contains_query,
    "Boolean Query": boolean_query,
    "Date Query": date_query,
    "Null Query": null_query,
    "Range Query": range_query,
    "Range 2 Query": range2_query,
    "String Equals Query": string_equals_query,
    "Number Equals Query": number_equals_query
}

translator = QueryToEnglish()

for name, q in queries.items():
    input_stream = InputStream(q)
    lexer = Esgish2GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Esgish2GrammarParser(token_stream)
    tree = parser.query()
    
    print(f"{name}: {translator.visit(tree)}\n")

