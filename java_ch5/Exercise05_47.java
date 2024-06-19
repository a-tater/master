import java.util.Scanner;

public class Exercise05_47 {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    System.out.print("Enter the first 12 digits of an ISBN-13 as a string: ");
    String ISBN = input.nextLine();
    int pos = 0;
    int checkSum = 0;
    int a = 0;
    int check = 0;
    boolean isISBN = false;

    if (ISBN.length() == 12) {
        isISBN = true;
        while (isISBN && pos < 12){
            if (Character.isDigit(ISBN.charAt(pos))) {
                a = Character.getNumericValue(ISBN.charAt(pos));
                if ((pos + 4) % 2 == 1){
                    check = (3*a);
                    checkSum += check;
                }
                else {
                    check = a;
                    checkSum += check;
                }
                pos ++;
            }
            else {
                isISBN = false;
            }
        }
    }
    if (isISBN){
        int chksm = 10 - (checkSum % 10);
        if (chksm == 10) {
            chksm = 0;
            System.out.println("The ISBN-13 number is " + ISBN + chksm);
            System.exit(0);
        }
        else {
            System.out.println("The ISBN-13 number is " + ISBN + chksm);
            System.exit(0);
        }           
    }
    else{
        System.out.println(ISBN + " is an invalid input");
        System.exit(0);
    }
  }
}
