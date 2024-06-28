// varType[] arrayName;
// varType[] arrayName = new[arraySize];
// arrayName[arrayIndex] = indexValue;

// ex int[] myList; - creates empty array of integers
// ex int[] myList = new[40]; - creates an array and allocates memory for 40 integers
// ex new[0] = 45;-inserts integer with value of 45 into first space of array

// arrayName.length
// ex myList.length;

// access variable myList[0] -accesses variable in first position of array

// array initializer
// ex varType[] arrayName = {value0, value1, value3, ...};


/*
  double[] myList = {4, 5, 6, 7, 8, 9};
  double temp = myList[0]; // Retain the first element

  // Shift elements left
  for (int i = 1; i < myList.length; i++) {
    myList[i - 1] = myList[i];
  }
  
  // Move the first element to fill in the last position
  myList[myList.length - 1] = temp;
 */


 /*
  * for each loops
  for (varType e: arrayName) {
    System.out.println(e);
  }
  */

  public class AnalyzeNumbers {
    public static void main(String[] args) {
      java.util.Scanner input = new java.util.Scanner(System.in);
      System.out.print("Enter the number of items: ");
      int n = input.nextInt(); 
      double[] numbers = new double[n]; // Create an array
      double sum = 0;
  
      System.out.print("Enter the numbers: ");
      for (int i = 0; i < n; i++) {
        numbers[i] = input.nextDouble();
        sum += numbers[i];
      }
      
      double average = sum / n;
  
      int count = 0; // The numbers of elements above average
      for (int i = 0; i < n; i++) 
        if (numbers[i] > average) // Count if number[i] > average
          count++;
  
      System.out.println("Average is " + average);
      System.out.println("Number of elements above the average is "
        + count);
    }
  }