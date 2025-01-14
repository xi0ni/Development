import java.util.Random;
import java.util.Scanner;

public class Hangman {

    Scanner input = new Scanner(System.in);
    String word;
    int guesses;
    boolean x;
    String placeholder;
    

    public Hangman() {
        this.x = true;
        this.guesses = 5;
        this.placeholder = " ";

        String[] words = {"george", "apple", "banana"};
        Random random = new Random();
        this.word = words[random.nextInt(words.length)];

        for (int i = 0; i < (word.length()-1); i++) {
            this.placeholder += "-";
        }

        System.out.println("placeholder: " + this.placeholder);
        while (x == true) {
            System.out.print("pick a letter: ");
            String letter = input.nextLine();
            System.out.println();
            
            
            if (word.contains(letter)) {
                for (int i = 0; i < word.length(); i++) {
                    if (word.substring(i, i + 1).equals(letter)) {
                        this.placeholder = this.placeholder.substring(0, i) + letter + this.placeholder.substring(i + 1);
                    }

                    if(this.placeholder.equals(this.word)){
                        System.out.println("you win");
                        x = false;
                    }
                }
            }
            else {
                this.guesses -= 1;
                System.out.println("wrong guess, you have " + this.guesses + " guesses left");

                if (this.guesses == 0) {
                    System.out.println("you lose");
                    x = false;
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
