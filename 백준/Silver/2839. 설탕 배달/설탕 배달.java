import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());

        if (A == 4 || A == 7) System.out.println(-1);
        else if (A % 5 == 0) System.out.println(A / 5);
        else if (A % 5 == 1 || A % 5 == 3) System.out.println(A / 5 + 1);
        else if (A % 5 == 2 || A % 5 == 4) System.out.println(A / 5 + 2);

    }
}