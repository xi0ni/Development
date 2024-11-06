import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        String filepath = "output.txt";  // The file you are working with
        try {
            // Create a BufferedWriter to write to output.txt
            BufferedWriter writer = new BufferedWriter(new FileWriter(filepath));

            // Create a File object to check if the file exists
            File file = new File(filepath); 
            if (!file.exists()) {
                System.out.println("File does not exist: " + filepath);
                return;
            }

            // Print the URL for the file to open in Chrome
            String fileUrl = file.toURI().toString();
            System.out.println("Open the file in Chrome with this link: " + fileUrl);

            // Write content to output.txt
            writer.write("look now");
            writer.close(); 

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
