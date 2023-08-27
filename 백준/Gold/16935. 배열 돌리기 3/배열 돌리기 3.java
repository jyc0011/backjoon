import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int R = scanner.nextInt();
        
        int[][] arr = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }
        
        for (int i = 0; i < R; i++) {
            int op = scanner.nextInt();
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
                    int temp2 = N; // We need to declare a new variable name as we can't reuse the same one in the same switch scope.
                    N = M;
                    M = temp2;
                    arr = rotate90(rotate90(rotate90(arr)));
                    break;
                case 5:
                    int[][][] divided1 = divide(arr);  // Similar to the previous comment, using a different variable name for scope reasons.
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