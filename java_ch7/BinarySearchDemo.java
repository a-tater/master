public class BinarySearchDemo {
	public static void main(String[] args) {
	  int[] list = {2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79};
	  System.out.println("1. Index is " +
		java.util.Arrays.binarySearch(list, 11));
	  System.out.println("2. Index is " +
		java.util.Arrays.binarySearch(list, 12));
			
	  char[] chars = {'a', 'c', 'g', 'x', 'y', 'z'};
	  System.out.println("3. Index is " +
		java.util.Arrays.binarySearch(chars, 'a'));
	  System.out.println("4. Index is " +
		java.util.Arrays.binarySearch(chars, 't'));
	}
  }

/*
 * java.util.Arrays.sort(arrayName);
 * java.util.Arrays.parallelSort(arrayName) -efficient if computer has multiple processors
 * java.util.Arrays.equals(array1, array2) - true or false
 * java.util.Arrays.fill(arrayName, 5) -fills 5 to the whole arra
 * java.util.Arrays.fill(arrayName, 1,5,8) -fills 8 to partial array
 * java.util.Arrays.toString(arrayName)
 */