import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 좌표가 몇사분면에 있는지 알아보시오.

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();

        if (x > 0){
            if (y > 0 ){
                System.out.println(1);
            }
            else{
                System.out.println(4);
            }
        }
        if (x < 0){
            if (y > 0){
                System.out.println(2);
            }
            else {
                System.out.println(3);
            }
        }
    }

}
