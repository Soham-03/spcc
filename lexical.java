import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class lexical{
    private static final String KEYWORDS = "if|else|while";
    private static final String OPERATORS = "\\+|-|\\*|/";
    private static final String INTEGERS = "\\d+";
    private static final String IDENTIFIERS = "[a-zA-Z]\\w*";
    private static final String TOKEN_PATTERNS =
            String.format("(%s)|(%s)|(%s)|(%s)", KEYWORDS, OPERATORS, INTEGERS, IDENTIFIERS);

    private static List<Token> tokenize(String input){
        List<Token> tokens = new ArrayList<>();
        Pattern tokenPattern = Pattern.compile(TOKEN_PATTERNS);
        Matcher matcher = tokenPattern.matcher(input);

        while(matcher.find()){
            if(matcher.group(1)!=null){
                tokens.add(new Token("KEYWORD", matcher.group(1)));
            }
            else if(matcher.group(2) != null){
                tokens.add(new Token("OPERATOR", matcher.group(2)));
            }
            else if(matcher.group(3) != null){
                tokens.add(new Token("INTEGERS", matcher.group(3)));
            }
            else if(matcher.group(4) != null){
                tokens.add(new Token("IDENTIFIERS", matcher.group(4)));
            }
        }
        return tokens;
    }

    private static class Token {
        private String type;
        private final String value;

        public Token(String type, String value) {
            this.type = type;
            this.value = value;
        }

        public String getType() {
            return type;
        }

        public String getValue() {
            return value;
        }
    }

    public static void main(String[] args) {
        String input = "if (a12 + 3) { while 7 }";
        List<Token> tokens = tokenize(input);
        tokens.forEach(token -> System.out.println(token.getType()+":"+token.getValue()));
    }
}