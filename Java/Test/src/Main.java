public class Main {
    public static void main(String[] args) {
        int num = 20; // Starting number (inclusive)
        while (num >= 0) {
            if (num % 2 == 0) {
                System.out.println(num);
            }
            num--;
        }

        for (int i = 20; i >= 0; i--) { 
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
        
}
