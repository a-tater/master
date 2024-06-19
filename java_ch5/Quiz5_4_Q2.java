/*
 Write a loop that reads positive integers from standard input, printing out those values that are greater than 100, each followed by a space, and that terminates when it reads an integer that is not positive.
Declare any variables that are needed.
Assume the availability of a variable stdin that references a Scanner object associated with standard input. That is, Scanner stdin = new Scanner(System.in); is given.
Don’t use any prompting message such as System.out.print("Enter an integer: ") in your code.
 */

import java.util.Scanner;

public class Quiz5_4_Q2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("enter a variable: ");
        int stdin = 5;
        String oPut = "";
        while (stdin > 0){
            stdin = input.nextInt();
            if (stdin > 100){
                oPut += String.valueOf(stdin);
                oPut += " ";
            }
        }
        System.out.println(oPut);
    }
}