
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = 14;
        while(!(n%3 == 0 && n%5 == 0 )){
            System.out.println(n);
            n += 2;
        }

        int a = 0;
        int b = 0;

        while(a < 5 && b < 3 ){
            System.out.println(a + " " + b);
            a++;
            b++;
        }

        System.out.println("do this");
        int numEntered = 0;
        int count = 0;
        while(numEntered != -1){
            numEntered = input.nextInt();
            count++;
        }
        System.out.println(count);
    }
}
