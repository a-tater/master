/*
(Format an integer)
Write a method with the following header to format the integer with the specified width.
public static String format(int number, int width)
The method returns a string for the number with one or more prefix 0s. The size of the string is the width.
For example,
format(34, 4)
 returns 
0034
format(34, 5)
 returns 
00034
If the number is longer than the width, the method returns the string representation for the number.
For example,
format(34, 1)
 returns 
34
Write a test program that prompts the user to enter a number and its width and displays a string returned by invoking 
format(number, width)
.
Sample Run
Enter an Integer: 34
Enter the width: 5
The formatted number is 00034
Class Name: 
Exercise06_37
 */

import java.util.Scanner;
public class Exercise06_37 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

        System.out.print("Enter an Integer: ");
        int num = input.nextInt();

        System.out.print("Enter the Width: ");
        int wid = input.nextInt();

        String answer = format(num, wid);

        System.out.println("The formatted number is " + answer);
	}

	public static String format(int number, int width) {
        String num = String.valueOf(number);
        String zero = "0";
        
        while (num.length() < width) {
            num = zero + num;
        }
        return num;
	}
}