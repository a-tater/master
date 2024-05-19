import java.util.Scanner;

public class SalesTax {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter purchase amount: ");
    double purchaseAmount = input.nextDouble();
    
    double tax = purchaseAmount * 0.06;
    System.out.println("Sales tax is " + (int)(tax * 100) / 100.0);

    System.out.println((int)(24.768 * 100) / 100.0);
    System.out.println((int)(24.768 * 100) / 100);

  }
} /* 
 int sum = 0;
 sum += 4.5; // sum becomes 4 after this statement
*/