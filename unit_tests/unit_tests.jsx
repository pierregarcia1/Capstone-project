function checkIfValid(query) {
    if (typeof query !== 'string' || query.includes('\n') || !/[a-zA-Z]/.test(query)) {
        return "Invalid input";
    }
    return "Valid input";
}

function testSearch(input, expected) {
    const result = checkIfValid(input);
    const isPassed = result === expected;
    console.log(`Unit test for input "${input}" ${isPassed ? 'passed' : 'failed'}`);
}

function testUserSearch() {
    testSearch("Show me entries where the number of board members is greater than 1", "Valid input");
    testSearch("Show me entries where the alcohol sales are greater than 3", "Valid input");

    testSearch(", ", "Invalid input");
    testSearch("\n", "Invalid input");
}

testUserSearch();
