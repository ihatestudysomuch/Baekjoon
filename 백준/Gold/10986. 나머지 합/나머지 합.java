/*

수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

첫 번째 줄 -> 수의 개수 N (0 < N < 10^6 +1 ), M( 1 < M < 10^3 + 1)
두 번째 줄 -> N개의 개수

 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        // 배열 A의 크기 N
        int N = Integer.parseInt(st.nextToken());
        // module M == 0
        int M = Integer.parseInt(st.nextToken());
        // module M의 값이 같은 index를 counting
        long[] C = new long[M];

        // 배열 A
        long[] A = new long[N];

        // st 초기화
        st = new StringTokenizer(bf.readLine());
        // A 만들기
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
//            System.out.print(A[i] + " ");
        }

        // 합배열 S
        long[] S = new long[N];
        S[0] = A[0];

        // S 만들기
        for (int i = 1; i < N; i++) {
            S[i] = S[i - 1] + A[i];
//            System.out.println(S[i]);
        }

        // M으로 나누어 떨어지면 ++
        long count = 0;

        for (int i = 0; i < N; i++) {
            // S[0~N]을 % M
            int module = (int) (S[i] % M);
            if (module == 0){
                count ++;
            }

            // module == 0 이면 나누어 떨어짐을 ++
            // module == 1 이면 나누면 1이 남음을 ++
            // 즉, module[0] = 3이면 나누어 떨어지는 값이 3개, module[1] = 1이면 나누어서 1이 남는 값이 1개인 것을 의미한다.
            C[module]++;
        }

        // 나누어 떨어지는 쌍의 개수
        for (int i = 0; i < M ; i++) {
            // 나머지가 i(i =0, < M , ++)인 값이 2개 이상 존재할 때(값의 쌍을 찾아야하니까)
            if (C[i] > 1){
                // count는 앞서 S[i] % M의 값에서 시작
                // S[i] % M = S[j] % M 이라면 원본 배열 A[i + 1]에서 A[j]까지의 합 % M의 값과도 같다.
                // 즉 S[i] % M의 값을 counting한 C[]에서 값이 같은 2개의 수를 뽑은 것과 같다. 조합공식
                // 아 뭔지 모르겠어서 그냥 외워야할 거 같아 ㅅ@발
                count =(count + (C[i] * (C[i] - 1) / 2));
            }
        }

        System.out.println(count);
    }
}
