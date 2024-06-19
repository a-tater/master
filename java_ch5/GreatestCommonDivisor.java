import java.util.Scanner; 

public class GreatestCommonDivisor {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter two integers
    System.out.print("Enter first integer: ");
    int n1 = input.nextInt();
    System.out.print("Enter second integer: ");
    int n2 = input.nextInt();

    int gcd = 1;
    int k = 2;
    while (k <= n1 && k <= n2) {
      if (n1 % k == 0 && n2 % k == 0)
        gcd = k;
      k++;
    }

    System.out.println("The greatest common divisor for " + n1 +
      " and " + n2 + " is " + gcd);

    int gcd2 = 1;
    int k2 = 2;
    for (int k1 = 2; k1 <= n1 && k1 <= n2; k2++) {
        if (n1 % k2 == 0 && n2 % k == 0)
            gcd2 = k;
    }
    System.out.println("The gcd2 for " + n1 + " and " + n2 + " is " + gcd2);
  }
}