import java.util.Scanner;

public class Quiz5_5Q1 {
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);
    String max = input.nextLine();
    while (input.hasNextLine()) {
        if (input.nextLine() != ""){
            max += " ";
            max += input.nextLine();      
        }
    }
    System.out.println(max);
  } // ctl z then enter to terminate program
}

