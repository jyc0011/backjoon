import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        int[] switchArray = new int[total];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < total; i++)
            switchArray[i] = Integer.parseInt(st.nextToken());

        int stuCnt = Integer.parseInt(br.readLine());
        for (int i = 0; i < stuCnt; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int number = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                boy(switchArray, total, number);
            } else {
                girl(switchArray, total, number);
            }
        }

        for (int i = 0; i < total; i++) {
            System.out.print(switchArray[i] + " ");
            if ((i + 1) % 20 == 0)
                System.out.println();
        }
    }

    private static void boy(int[] switchArray, int total, int number) {
        for (int j = 0; j < total; j++) {
            if ((j + 1) % number == 0)
                switchArray[j] ^= 1;
        }
    }

    private static void girl(int[] switchArray, int total, int number) {
        switchArray[number - 1] ^= 1;
        for (int j = 1; j < total / 2; j++) {
            if (number - 1 + j >= total || number - 1 - j < 0)
                break;
            if (switchArray[number - 1 - j] == switchArray[number - 1 + j]) {
                switchArray[number - 1 - j] ^= 1;
                switchArray[number - 1 + j] ^= 1;
            } else break;
        }
    }
}
