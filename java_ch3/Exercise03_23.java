import java.util.Scanner;

public class Exercise03_23 {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter a point with two coordinates: ");
    String point = input.nextLine();
    
    String[] points = point.trim().split(" ");

    double p1 = Double.parseDouble(points[0]);
    double p2 = Double.parseDouble(points[1]);



    if ((p1 >= -5 && p1 <= 5) && (p2 >= -2.5 && p2 <= 2.5))
        System.out.println("Point (" + p1 + ", " + p2 + ") is in the rectangle");
    else
        System.out.println("Point (" + p1 + ", " + p2 + ") is not in the rectangle");
  }
}