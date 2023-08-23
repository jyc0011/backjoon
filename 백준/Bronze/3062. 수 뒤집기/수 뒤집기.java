import java.io.*;

public class Main {

    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int testCaseCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCaseCount; i++) {
            bw.write(isPalindromeSum() ? "YES" : "NO");
            if (i != testCaseCount - 1) bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    static boolean isPalindromeSum() throws IOException {
        StringBuilder sb = new StringBuilder(br.readLine());
        int original = Integer.parseInt(sb.toString());
        int reversed = Integer.parseInt(sb.reverse().toString());
        int sum = original + reversed;
        return isPalindrome(sum);
    }

    static boolean isPalindrome(int number) {
        String str = Integer.toString(number);
        int len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}