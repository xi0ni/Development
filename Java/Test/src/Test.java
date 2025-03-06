
import java.util.ArrayList;

public class Test {      
static void shiftLeft(ArrayList<String> words){
  String temp = null;
  if (words.size() > 1) { 
    String first = words.remove(0);  
    words.add(first);  
      }

    System.out.println(words);
    }
} 