import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 2 integers:");
        
        int x = input.nextInt();
        int y = input.nextInt();
        
        if (y == 0) {
            System.out.println("Division by zero is not allowed.");
        } else {
            double ratio = (double) x / y; 
            if (ratio > 1 && ratio <= 8) {
                System.out.println("Ratio OK");
            }
        }
        
        input.close();
    }
    }

