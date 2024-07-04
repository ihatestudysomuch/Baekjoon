/*

N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

첫 번째 줄 -> 크기 N ( 0 < N < 1024 ) 과 합을 구해야 하는 횟수 M ( 0 < M < 100,000 )
두 번째 줄 ~ -> 표에 집어넣을 value와 구간합의 크기

 */

// package Baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
//        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//        String[] s = bf.readLine().split(" ");
//        // N * N의 배열의 크기
//        int N = Integer.parseInt(s[0]);
//        // M번의 구간합 연산
//        int M = Integer.parseInt(s[1]);
//
//        // 배열 A
//        int[][] A = new int[N + 1][N + 1];
//
//        // 배열 A 만들기
//        for (int i = 1; i <= N; i++) {
//            String[] ss = bf.readLine().split(" ");
//            for (int j = 1; j <= N; j++) {
//                // 왜 ss[j - 1]? -> String[] ss는 index가 0부터 시작이니까!
//                A[i][j] = Integer.parseInt(ss[j - 1]);
////                System.out.println(A[i][j]);
//            }
//        }
//
//        // 합배열 S
//        int[][] S = new int[N + 1][N + 1];
//
//        // 합배열 S 만들기
//        for (int i = 1; i < N + 1 ; i++) {
//            for (int j = 1; j < N + 1; j++) {
//                S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + A[i][j];
//                System.out.println(S[i][j]);
//            }
//        }
//
//        // M번의 횟수만큼 (x1,y1) (x2,y2)범위의 구간합 구하기
//        for (int i = 0; i < M; i++) {
//            String[] sss = bf.readLine().split(" ");
//
//            int x1 = Integer.parseInt(sss[0]);
//            int y1 = Integer.parseInt(sss[1]);
//
//            int x2 = Integer.parseInt(sss[2]);
//            int y2 = Integer.parseInt(sss[3]);
//            System.out.println(x1 + " " + y1 + " " + x2 + " " + y2);
//
//            // (x1,y1) (x2,y2) 구간합 구하는 공식
//            System.out.println(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 -1]);
//        }
        BufferedReader bf =  new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        // N * N의 배열의 크기
        int N = Integer.parseInt(st.nextToken());
        // M번의 구간합 연산
        int M = Integer.parseInt(st.nextToken());

        // System.out.println(N + " " + M);
        // 배열 A
        int[][] A = new int[N + 1][N + 1];

        // 배열 A 만들기
        for (int i = 1; i < N + 1 ; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 1; j < N + 1; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 합배열 S
        int[][] S = new int[N + 1][N + 1];

        // 합배열 S 만들기
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                S[i][j] = S[i - 1][j] + S[i][j - 1] + A[i][j] - S[i - 1][j - 1];
            }
        }

        // (X1,Y1) (X2,Y2)의 구간합 구하기
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int sum = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1];
            System.out.println(sum);
        }
    }
}