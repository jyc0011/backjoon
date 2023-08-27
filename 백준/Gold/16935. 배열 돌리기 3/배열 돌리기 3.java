import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        String[] strs = br.readLine().split(" ");
        for (int i = 0; i < R; i++) {
            int op = Integer.parseInt(strs[i]);
            switch (op) {
                case 1:
                    arr = flip(rotate90(rotate90(arr)));
                    break;
                case 2:
                    arr = flip(arr);
                    break;
                case 3:
                    int temp = N;
                    N = M;
                    M = temp;
                    arr = rotate90(arr);
                    break;
                case 4:
                    int temp2 = N;
                    N = M;
                    M = temp2;
                    arr = rotate90(rotate90(rotate90(arr)));
                    break;
                case 5:
                    int[][][] divided1 = divide(arr);
                    arr = combine(divided1[2], divided1[0], divided1[3], divided1[1]);
                    break;
                case 6:
                    int[][][] divided2 = divide(arr);
                    arr = combine(divided2[1], divided2[3], divided2[0], divided2[2]);
                    break;
            }
            
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] rotate90(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] result = new int[cols][rows];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[j][rows - 1 - i] = matrix[i][j];
            }
        }
        
        return result;
    }

    public static int[][] flip(int[][] matrix) {
        int rows = matrix.length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0, k = matrix[i].length - 1; j < k; j++, k--) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][k];
                matrix[i][k] = temp;
            }
        }
        return matrix;
    }

    public static int[][][] divide(int[][] array) {
        int n = array.length;
        int m = array[0].length;
        
        int[][] q1 = new int[n/2][m/2];
        int[][] q2 = new int[n/2][m/2];
        int[][] q3 = new int[n/2][m/2];
        int[][] q4 = new int[n/2][m/2];
        
        for (int i = 0; i < n/2; i++) {
            for (int j = 0; j < m/2; j++) {
                q1[i][j] = array[i][j];
                q2[i][j] = array[i][j + m/2];
                q3[i][j] = array[i + n/2][j];
                q4[i][j] = array[i + n/2][j + m/2];
            }
        }
        return new int[][][]{q1, q2, q3, q4};
    }

    public static int[][] combine(int[][] q1, int[][] q2, int[][] q3, int[][] q4) {
        int n = q1.length + q3.length;
        int m = q1[0].length + q2[0].length;
        
        int[][] result = new int[n][m];
        for (int i = 0; i < n/2; i++) {
            for (int j = 0; j < m/2; j++) {
                result[i][j] = q1[i][j];
                result[i][j + m/2] = q2[i][j];
                result[i + n/2][j] = q3[i][j];
                result[i + n/2][j + m/2] = q4[i][j];
            }
        }
        return result;
    }
}