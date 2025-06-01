
import java.util.ArrayList;

public class Test {
  private double balance;

  public Test() {
      balance = 0;
  }

  public Test(double acctBalance) {
      balance = acctBalance;
  }

  public void deposit(double amount) {
      balance += amount;
  }

  public void withdraw(double amount) {
      balance -= amount;
  }

  public double getBalance() {
      return balance;
  }
}





