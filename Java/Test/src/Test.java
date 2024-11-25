public class Test {
    private int n;
    private int sum;

    public Test(int n) {
        this.n = n; 
        this.sum = 0; 
    }

    public void initialize() {
        for (int i = 1; i < 100; i++) { 
            if (n % i != 0) {
                sum++;
                System.out.println(i); 
            }
        }
        System.out.println(sum);
    }
}

