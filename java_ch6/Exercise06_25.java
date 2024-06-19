/*
(Convert milliseconds to hours, minutes, and seconds)
Write a method that converts milliseconds to hours, minutes, and seconds using the following header:
public static String convertMillis(long millis)
The method returns a string as 
hours:minutes:seconds
.
For example,
convertMillis(5500)
 returns a string 
0:0:5
,
convertMillis(100000)
 returns a string 
0:1:40
convertMillis(555550000)
 returns a string 
154:19:10
.
Write a test program that prompts the user to enter a long integer for milliseconds and displays a string in the format of hours:minutes:seconds.
Sample Run
Enter time in milliseconds: 555550000
154:19:10
 */

import java.util.Scanner;
public class Exercise06_25 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.println("Enter a long integer to convert to time: ");

		long millis = input.nextLong();

		String answer = convertMillis(millis);
		
		System.out.println(answer);

	}

	public static String convertMillis(long millis){
		String ansr;

		double seconds = Math.floor(millis * .001);
		//System.out.println(seconds);
		
		double secs = seconds % 60;
		//System.out.println(secs);

		double minutes = Math.floor(seconds / 60);
		double mins = Math.floor(minutes % 60);
		//System.out.println(mins);

		double hours = Math.floor(minutes / 60);
		//System.out.println(hours);

		ansr = (int)hours + ":" + (int)mins + ":" + (int)secs;
		return ansr;
	}
}