import java.util.Scanner;

public class Exercise7_19 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the size of the list: ");

        int listSize = input.nextInt();
        int[] amISorted = new int[listSize];

        System.out.print("Enter the contents of the list: ");

        for (int i=0; i < listSize; i++) {
            amISorted[i] = input.nextInt();
        }
        
        System.out.print("The list has " + listSize + " integers");
        for (int i=0; i < listSize; i++)
            System.out.print(" " + amISorted[i]);

        boolean isItSorted = isSorted(amISorted);

        if (isItSorted)
            System.out.println("\nThe list is already sorted");
        else
            System.out.println("\nThe list is not sorted");
    }

    public static boolean isSorted(int[] list) {
        int lower = list[0];
        for (int i=1; i < list.length; i++) {
            if (list[i] < lower)
                return false;
            else 
                lower = list[i];
        }
        return true;
    }
}