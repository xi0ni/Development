public class Test {
    private int n;
    private int sum;

    public Test(int n) {
        this.n = n; 
        this.sum = 0; 
    }

    public void initialize() {
        while (n > 0) {
            sum += n % 10;
            n /= 10;     
        }

        System.out.println(sum);
    }
}

