public class TestScannerNextLine {
    public static void main(String[] args) {
      java.util.Scanner input = new java.util.Scanner(System.in); 
      System.out.print("Enter a line: "); 
      String s = input.nextLine(); // Read a line
      System.out.println("The line entered is " + s);
    }
  }