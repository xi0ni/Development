import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> words = new ArrayList<>();
        words.add("george");
        words.add("poop");
        words.add("leon");
        words.add("e");
        
        /*System.out.println("Please enter words, enter STOP to stop the loop.");
        String input = scan.nextLine();
        
        while (!input.equals("STOP")) {
            words.add(input);
            input = scan.nextLine();
        }*/
        System.out.println(words);
        Test.shiftLeft(words);
        
        
        scan.close();
    }
}
