    /*
    
    수 N개가 주어졌을 때, i 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
    
    첫 번째 줄 -> 수의 개수 N (0 < N < 100,001), 합을 구해야 하는 횟수 M (0 < M < 100,001)
    두 번째 줄 -> N개의 수
    세 번째 줄 ~ -> 합을 구해야 하는 구간인 i ~ j
     */
    
//    package Baekjoon.Array;
    
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    
            // 첫 번째 줄에 입력할 수의 개수 N과 합을 구해야하는 횟수 M의 입력을 위한 input
            String[] input = bf.readLine().split(" ");
    
    
            // 수의 개수 N
            int N = Integer.parseInt(input[0]);
            // 합을 구해야 하는 횟수 M
            int M = Integer.parseInt(input[1]);
            // N의 value값을 저장할 A
            int[] A = new int[N+1];
    
    //        System.out.println(N + " " + M);
    
            // A 배열의 value를 저장하기 위해
            String[] inputA = bf.readLine().split(" ");
    
            // 배열 A 완성
            for (int i = 1; i <= N; i++) {
                A[i] = Integer.parseInt(inputA[i - 1]);
    //            System.out.print(A[i] + " ");
            }
    
            // 합배열 S
            int[] S = new int[N + 1];
    
            // 합배열 S의 완성
            for (int i = 1; i < N + 1 ; i++) {
                S[i] = S[i - 1] + A[i];
    //               System.out.print(S[i] + " ");
            }
           
    
            for (int k = 0; k < M; k++) {
                String[] ij = bf.readLine().split(" ");
                // i와 j값 설정
                int i = Integer.parseInt(ij[0]);
                int j = Integer.parseInt(ij[1]);
                // 구간합 출력
                System.out.println(S[j] - S[i -1]);
            }
    
        }
    }
