import java.util.Scanner;

public class Exercise02_05 {
  public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	System.out.print("Enter subtotal: ");
	double subTotal = input.nextDouble();

	System.out.print("Enter gratuity rate: ");
	double gratuity = input.nextDouble() * subTotal / 100.0;
	
	double total = subTotal + gratuity;
	System.out.println("The gratuity is $" + gratuity + " and total is $" + total);

  }
}