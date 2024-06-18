import java.util.Scanner;

public class Exercise05_01 {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    System.out.println("Enter an integer, the input ends if it is 0: ");

    int numberOfPositives = 0;
    int numberOfNegatives = 0;
    int total = 0;
    float count = 0;

    int num = input.nextInt();
    if (num == 0) {
        System.out.println("No numbers are entered except 0");
        System.exit(0);
    }

    while (num != 0) {
        if (num > 0)
            numberOfPositives++;
        else
            numberOfNegatives++;
        total += num;
        count ++;
        num = input.nextInt();
    }
    System.out.println("The number of positives is " + numberOfPositives);
    System.out.println("The number of negatives is " + numberOfNegatives);
    System.out.println("The total is " + total);
    float average = total / count;
    System.out.println("The average is " + average);

  }
}