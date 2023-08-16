import java.io.*;

public class Solution {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            int qCount = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < qCount; i++) {
                int qNum = Integer.parseInt(br.readLine().trim());
                String[] parts = br.readLine().trim().split(" ");
                int mode = findMode(parts);
                bw.write("#" + qNum + " " + mode + "\n");
            }
            bw.flush();
            bw.close();
        } catch (IOException e) {
            System.out.println("Error occurred.");
            e.printStackTrace();
        }
    }

    public static int findMode(String[] parts) {
        int[] freq = new int[101];
        for (String part : parts) {
            freq[Integer.parseInt(part)]++;
        }
        int mode = 0;
        for (int i = 1; i < freq.length; i++) {
            if (freq[i] >= freq[mode]) {  // Here, changed the condition to >= so in case of a tie, the highest number wins.
                mode = i;
            }
        }
        return mode;
    }
}