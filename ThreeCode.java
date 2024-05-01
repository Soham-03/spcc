import java.util.*;

public class ThreeCode{
    private int tempCounter = 0;

    // Method to create a new temporary variable
    private String newTemp() {
        return "t" + tempCounter++;
    }

    // Generate three-address code for a given expression
    public void generateTAC(String expr) {
        Stack<String> stack = new Stack<>();
        String[] tokens = expr.split(" ");

        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                // Pop two operands from the stack
                String right = stack.pop();
                String left = stack.pop();

                // Create a new temporary variable
                String temp = newTemp();

                // Generate the TAC instruction
                System.out.println(temp + " = " + left + " " + token + " " + right);

                // Push the result (temporary variable) back onto the stack
                stack.push(temp);
            } else {
                // Push operands and variables directly onto the stack
                stack.push(token);
            }
        }

        // The last element in the stack is the final result
        if (!stack.isEmpty()) {
            String result = stack.pop();
            System.out.println("Result = " + result);
        }
    }

    public static void main(String[] args) {
        ThreeCode tacGenerator = new ThreeCode();
        // Example expression: fully parenthesized to ensure order
        String expression = "a b + c *";
        tacGenerator.generateTAC(expression);
    }
}

