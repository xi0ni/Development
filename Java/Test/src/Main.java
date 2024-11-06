import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            // Reading from input.txt and printing its content
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            reader.close();

            // Writing an initial line to output.txt
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));
            writer.write("This is a new line.");
            writer.newLine(); // Adds a new line
            writer.close();

            // Reading all lines from output.txt
            List<String> lines = new ArrayList<>();
            BufferedReader outputReader = new BufferedReader(new FileReader("output.txt"));
            while ((line = outputReader.readLine()) != null) {
                lines.add(line);
            }
            outputReader.close();

            // Modifying a specific line (e.g., changing the first line)
            if (lines.isEmpty()) {
               lines.set(0, "money: 4"); // Modify the first line
            }

            // Writing all lines back to output.txt
            BufferedWriter outputWriter = new BufferedWriter(new FileWriter("output.txt"));
            for (String modifiedLine : lines) {
                outputWriter.write(modifiedLine);
                outputWriter.newLine();
            }
            outputWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
