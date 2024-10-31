import java.util.Scanner;

public class Main {
       public static void main(String[] args)
       {
          Scanner input = new Scanner(System.in);
          
          System.out.println("latitude: ");
          double latitude = input.nextDouble();
          System.out.println("longitude: ");
          double longitude = input.nextDouble();
          
          if (latitude < -90 || latitude > 90) {
             System.out.println("latitude is incorrect");
          }
          if (longitude < -180 || longitude > 180) {
             System.out.println("longitude is incorrect");
          }
          
          if (latitude >= -90 && latitude <= 90 && longitude >= -180 && longitude <= 180) {
             System.out.println("The location: " + latitude + " , " + longitude);
          }
       }
    }

    


