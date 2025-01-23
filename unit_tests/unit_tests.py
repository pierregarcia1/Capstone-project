def check_if_valid(query):
    if not isinstance(query, str) or '\n' in query or not any(c.isalpha() for c in query):
        return "Invalid input"
    return "Valid input"

def test_search(input_query, expected):
    result = check_if_valid(input_query)
    is_passed = result == expected
    print(f'Unit test for search "{input_query}" {"passed" if is_passed else "failed"}')

def test_user_search():
    test_search("Show me entries where the number of board members is greater than 1", "Valid input")
    test_search("Show me entries where the alcohol sales are greater than 3", "Valid input")


    test_search(", ", "Invalid input")
    test_search("\n", "Invalid input")

if __name__ == "__main__":
    test_user_search()
