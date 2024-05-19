import java.util.Scanner;

public class Exercise02_21 {
  public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	System.out.print("Enter investment amount: ");
	double investmentAmount = input.nextDouble();

	System.out.print("Enter annual interest rate: ");
	double monthlyInterestRate = input.nextDouble() / 1200;

	System.out.print("Enter number of years: ");
	double numberOfYears = input.nextDouble();

    double futureInvestmentValue = investmentAmount * Math.pow((1 + monthlyInterestRate),(numberOfYears * 12));
	
	System.out.println("Future value is $" + (int)(futureInvestmentValue * 100) / 100.0);

  }
}