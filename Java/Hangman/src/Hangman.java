import java.util.Scanner;

public class Hangman {

    Scanner input = new Scanner(System.in);
    String word;
    int guesses;
    boolean x;
    String placeholder;

    public Hangman() {
        this.x = true;
        this.word = "george";
        this.guesses = 5;
        this.placeholder = " ";

        for (int i = 0; i < word.length(); i++) {
            this.placeholder += "_ ";
        }

        System.out.println("placeholder: " + this.placeholder);
        while (x == true) {
            System.out.print("pick a letter: ");
            String letter = input.nextLine();
            System.out.println("");
            
            
            if (word.contains(letter)) {
                for (int i = 0; i < word.length(); i++) {
                    if (word.substring(i, i + 1).equals(letter)) {
                        this.placeholder = this.placeholder.substring(0, i) + letter + this.placeholder.substring(i + 1);
                    }
                }
            }
            

            System.out.println("placeholder: " + this.placeholder);







            if(letter.equals("stop")){
                x = false;
            }
        }
    }



    public void initialize() {
        
    }

}
