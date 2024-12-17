public class MyInterger {

    int value = 1;
    boolean isPrime = true;
    public MyInterger(int val){
        this.value = val;
    }

    public void isEven(){
        

        if (this.value %2 ==0){
            System.out.println("is even");
        }
        else{
            System.out.println("not even");
        }
    }

    public void isOdd(){
        this.value = this.value;

        if (this.value %2 ==1){
            System.out.println("is odd");
        }
        else{
            System.out.println("not odd");
        }
    }

    public void isPrime(){
        this.value = this.value;

        for(int i = 2; i<this.value;i++){
            if(this.value%i == 0){
            boolean isPrime = false;
            }
        }

        if(isPrime = true){
            System.out.println("It is a prime number");
        }
        else{
            System.out.println("It is not a prime number");
        }
    }

    public static void main(String[] args) {
        MyInterger number = new MyInterger(21);
        number.isEven();
        number.isOdd();
        number.isPrime();
    }

}
