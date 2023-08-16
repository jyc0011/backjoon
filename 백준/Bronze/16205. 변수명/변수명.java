import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int choice = Integer.parseInt(input[0]);
        String original = input[1];
        
        StringBuilder sb = new StringBuilder(original);

        switch (choice){
            case 1:
                System.out.println(sb);
                toSnake(sb);
                System.out.println(sb);
                toPascal(sb);
                System.out.println(sb);
                break;
            case 2:
                toCamel(sb);
                System.out.println(sb);
                System.out.println(original);
                toPascal(sb);
                System.out.println(sb);
                break;
            case 3:
                sb.setCharAt(0, Character.toLowerCase(sb.charAt(0)));
                System.out.println(sb);
                toSnake(sb);
                System.out.println(sb);
                toPascal(sb);
                System.out.println(sb);
                break;
        }
    }

    private static void toSnake(StringBuilder s) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c) && i != 0) {
                s.insert(i++, '_');
            }
            s.setCharAt(i, Character.toLowerCase(c));
        }
    }

    private static void toCamel(StringBuilder s) {
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '_') {
                char nextC = s.charAt(i + 1);
                s.deleteCharAt(i);
                s.setCharAt(i, Character.toUpperCase(nextC));
            }
        }
    }

    private static void toPascal(StringBuilder s) {
        s.setCharAt(0, Character.toUpperCase(s.charAt(0)));
        toCamel(s);
    }
}
