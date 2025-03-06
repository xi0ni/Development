import java.util.*;

public class ContainsNeg {
    public static boolean containsNeg(double[] arr)
    {
        for(int i=0; i < arr.length; i++){
            if(arr[i] <= 0){
                System.out.println("False");
                return false;
            }
        }
        System.out.println("True");
        return true;
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter array length: ");
        int length = input.nextInt();

        double[] arr = new double[length];
        System.out.println("Enter values: ");
        for(int i = 0; i < length; i++){
            
            arr[i] = input.nextDouble();
        }

        containsNeg(arr);
        
    }
}



/*In the U6_L2_Activity_One class, there is a method called containsNeg() that has a single parameter, 
arr, which is an array of double values. You will edit this method so that it returns a true if the 
array being passed contains a negative value and return a false otherwise.

The runner class already has code provided that will prompt the user for the array length, prompt
 for double values, and call and output the method you are creating. All you need to do is edit 
 the method in order to return the corresponding true or false value.

Sample runs (runner class):

Enter array length:
4
Enter values:
1.1
2.2
3.3
-4.4
Contains negative: true

Enter array length:
3
Enter values:
1.1
2.2
3.3
Contains negative: false */