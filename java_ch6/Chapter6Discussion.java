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
public class Chapter6Discussion {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

        int a = 1;
        int b = 2;

        System.out.print("Calling the add function results in " + add(a,b));
        System.out.print("Calling the add function results in " + add(0,1));
	}

    // pass-by-value
    public static int add(int a, int b) {
        return a + b;
    }

    public static int add1(int a) {

    }
}