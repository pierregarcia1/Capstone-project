public class unit_tests {

    public static String checkIfValid(String query) {
        if (query == null || query.contains("\n") || !query.matches(".*[a-zA-Z].*")) {
            return "Invalid input";
        }
        return "Valid input";
    }

    public static void testSearch(String input, String expected) {
        String result = checkIfValid(input);
        boolean isPassed = result.equals(expected);
        System.out.println("Unit test for input \"" + input + "\" " + (isPassed ? "passed" : "failed"));
    }

    public static void testUserSearch() {
        testSearch("Show me entries where the number of board members is greater than 1", "Valid input");
        testSearch("Show me entries where the alcohol sales are greater than 3", "Valid input");

        testSearch(", ", "Invalid input");
        testSearch("\n", "Invalid input");
    }

    public static void main(String[] args) {
        testUserSearch();
    }
}
