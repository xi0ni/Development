public class Test {
    public static void main(String[] args) {
        for (int k = 1; k <= 20; k++) {
           int n = (int)(40*Math.random());
           if(n%2 == 0) {
               System.out.println(n + " is even");
           } else {
               System.out.println(n + " is odd");
           }
        }
    }

}