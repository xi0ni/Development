import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
      Scanner input = new Scanner(System.in);
      
      System.out.println("latitude: ");
      Double int1 = input.nextDouble();
      System.out.println("longitude: ");
      Double int2 = input.nextDouble();
      
      if(int1 < -90 || int1 > 90){
        System.out.println("latitude is incorrect");
      if(int2 < -180 || int2 > 180){
          System.out.println("longitude is incorrect");
        }
        
  
      }
      else
      {
        System.out.println("The location:" + int1 + " , " + int2);
      }
      
    }
  }
  
  /*if((int1 >= 90 && int1<= 90) && (int2 >= -180 && int2 <= 180))*/


