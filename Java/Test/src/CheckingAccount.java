public class CheckingAccount extends Test {
    private static final double FEE = 2.0;
    private static final double MIN_BALANCE = 50.0;
  
    public CheckingAccount(double acctBalance) {
        // implementation not shown
    }
  
    /**
     * Fee of $2 deducted if withdraw leaves balance less than MIN_BALANCE.
     * Allows for negative balance.
     */
    public void withdraw(double amount) {
        // implementation not shown
    }
  }