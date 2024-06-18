/* 
    (Check SSN)
Write a program that prompts the user to enter a Social Security number in the format 
DDD-DD-DDDD, where D is a digit.
Your program should check whether the input is valid.
Sample Run 1
Enter a SSN: 232-23-5435
232-23-5435 is a valid social security number
Sample Run 2
Enter a SSN: 23-23-5435
23-23-5435 is an invalid social security number
Class Name: 
Exercise04_21
*/


// import java.util.Scanner;
public class testPower { 
    public static void main(String[] args) {
    // Scanner input = new Scanner(System.in);

    // System.out.print("Enter a SSN: ");
    // String ssn = input.nextLine();

    // String[] ssnSplit = ssn.trim().split("-");

    // int p0 = Integer.parseInt(ssnSplit[0]);
    // int p1 = Integer.parseInt(ssnSplit[1]);
    // int p2 = Integer.parseInt(ssnSplit[2]);

    // if ((100 <= p0 && p0 <= 999) && (10 <= p1 && p1 <= 99) && (1000 <= p2 && p2 <= 9999))
    //     System.out.println(ssn + " is a valid social security number");
    // else
    //     System.out.println(ssn + " is an invalid social security number");

        Double answer = Math.pow(1000, 1.03);
        System.out.println(answer);
    }
  }