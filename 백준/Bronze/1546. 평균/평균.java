import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

//        System.out.println("N: ");
        // 세준이의 시험 본 과목 수 N
        int N = Integer.parseInt(bf.readLine());
        // 세준이의 N개의 시험 성적
        int[] grade = new int[N];
        // 세준이의 성적 입력을 하기 위해 공백이 나올 때 마다 Index에 저장한다.
        String[] userInput = bf.readLine().split(" ");

        for (int i = 0; i < grade.length; i++) {
            // 세준이의 N개의 성적 입력
            // String type의 userInput을 Integer type으로 변환하여 grade에 저장
            grade[i] = Integer.parseInt(userInput[i]);
        }

        // 평균을 구하기 위한 성적의 합
        double sum = 0;
        // 세준이의 시험 성적 중에서 가장 큰 값
        int max = 0;

        for (int i = 0; i < grade.length; i++) {
            if (grade[i] > max){
                // 0으로 초기화된 max를 계속해서 큰 값으로 바꿔주면서 최종적으로 가장 큰 값을 가지도록 한다.
                max = grade[i];
            }
            // 세준이의 성적의 합
            sum += grade[i];
        }
//        System.out.println("sum: ");
        // 세준이가 조작한 시험 성적의 평균
        double avr = sum * 100.0 / max / N;

        System.out.println(avr);
    }
}