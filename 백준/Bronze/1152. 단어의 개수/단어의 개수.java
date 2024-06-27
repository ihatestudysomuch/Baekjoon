import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();
        text = text.trim();
        String[] ary = text.split(" ");
        if (text.equals("")) {
            System.out.println(0);
        } 
        else {
            System.out.println(ary.length);
        }

        sc.close();
    }
}
