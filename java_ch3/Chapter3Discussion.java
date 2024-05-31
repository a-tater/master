import java.util.Scanner;

public class Chapter3Discussion {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter a number between 1 and 100: ");
    int yourNum = input.nextInt();

    /*  nested if, multi-way if , switch statement*/

    if (yourNum < 5) {
        if (yourNum < 2) // this is a basic if statement
          System.out.println("Your number is the number 1!");
    }
    else if (yourNum < 50) {
      switch (yourNum) {
        case 10: System.out.println("Your number is ten!"); break;
        case 20: System.out.println("Your number is twenty!"); break;
        case 35: System.out.println("Your number is thirty!"); break;
        default: System.out.println("Your number is not ten, twenty, or thirty, but it's still less than fifty!");
          System.exit(1);
      }
    }
  }
}