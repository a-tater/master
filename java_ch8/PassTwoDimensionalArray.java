/*
 * elementType[][] arrayRefVar;
 * ex int[][] matrix; = two dimensional array of integers
 * matrix = new int[5][5]; = five arrays with five values each
 * [row_index][column_index] || top to bottom, left to right
 * assign values || matrix[2][7] = 7; assigns value of 7 to third row, eighth column
 * int[][] array = {
      {1, 2, 3},
      {4, 5, 6},
      {7, 8, 9},
      {10, 11, 12}
    };

    or

int[][] array = new int[4][3];
array[0][0] = 1; array[0][1] = 2; array[0][2] = 3; 
array[1][0] = 4; array[1][1] = 5; array[1][2] = 6; 
array[2][0] = 7; array[2][1] = 8; array[2][2] = 9; 
array[3][0] = 10; array[3][1] = 11; array[3][2] = 12;
*/

import java.util.Scanner;

public class PassTwoDimensionalArray {
  public static void main(String[] args) {
    int[][] m = getArray(); // Get an array

    // Display sum of elements
    System.out.println("\nSum of all elements is " + sum(m));
  }
  
  public static int[][] getArray() {
    // Create a Scanner
    Scanner input = new Scanner(System.in);
    
    // Enter array values
    int[][] m = new int[3][4];
    System.out.println("Enter " + m.length + " rows and "
      + m[0].length + " columns: ");
    for (int i = 0; i < m.length; i++)
      for (int j = 0; j < m[i].length; j++)
        m[i][j] = input.nextInt();

    return m;
  }

  public static int sum(int[][] m) {
    int total = 0;
    for (int row = 0; row < m.length; row++) {
      for (int column = 0; column < m[row].length; column++) {
        total += m[row][column];
      }
    }

    return total;
  }
}