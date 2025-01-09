public class Main {
    public static void main(String[] args) {
        int x = 0;
        while (x < 5) {
            int y = 5;
            while (x < y) {
                y--;
                x++;
            }
            System.out.print(y + " ");
        }
    }
}
