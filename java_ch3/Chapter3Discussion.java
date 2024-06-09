import java.util.Scanner;

public class Chapter3Discussion {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter a number between 1 and 100: ");
    int yourNum = input.nextInt();

    /*  nested if, multi-way if , switch statement*/

    if (yourNum < 5) { // this is a nested if
        if (yourNum < 2) // the nested if is wrapped in brackets and indented on the next line
          System.out.println("Your number is the number 1!");
    } // this bracket closes out the first if statement
    else if (yourNum < 50) { // for else if, drop a line, include the boolean test, and open another set of brackets
      switch (yourNum) { // this switch statement is nested in the else-if statement (includes a value to be tested against with case statments)
        case 10: System.out.println("Your number is ten!"); break; // if a case stement evaluates to true, the code to the right of the : is executed
        case 20: System.out.println("Your number is twenty!"); break; // in order to break out of the case statement, a break; is included after the code to be executed
        case 30: System.out.println("Your number is thirty!"); break;
        default: System.out.println("Your number is not ten, twenty, or thirty, but it's still less than fifty!"); // a default case runs in the same way an 'else' statement would execute
          System.exit(1); // the System.exit(1) allows the code to exit gracefully following the case statement
      }
    }
  }
}