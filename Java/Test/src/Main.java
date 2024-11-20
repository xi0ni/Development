
public class Main {
    public static void main(String[] args) {
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
    }
}
