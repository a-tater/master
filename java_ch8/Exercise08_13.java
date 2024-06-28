
import java.util.Scanner;

public class Exercise08_13 {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number of rows and columns of the array: ");

		int rows = input.nextInt();
		int columns = input.nextInt();

		double[][] myArray = new double[rows][columns];

        System.out.print("Enter the array: ");
        for (int i=0; i < myArray.length; i++) {
            for (int y=0; y < myArray[i].length; y++){
                myArray[i][y] = input.nextDouble();
            }
        }
        int[] answer = locateLargest(myArray);
        System.out.println("The location of the largest element is at (" + answer[0] + ", " + answer[1] + ")");
	}

    public static int[] locateLargest(double[][] a) {
        int[] arrayPosition = new int[2];
        double largest = a[0][0];
        double checkValue = 0;
        for (int i = 0; i < a.length; i++) {
            for (int y = 0; y < a[i].length; y++) {
                checkValue = a[i][y];
                if (checkValue > largest) {
                    arrayPosition[0] = i;
                    arrayPosition[1] = y;
                    largest = checkValue;
                }
            }
        }
        return arrayPosition;
    }
}