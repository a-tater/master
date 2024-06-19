import java.util.Scanner;

public class PreTestPostTestLoop {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    int a = 2;
    int b = 2;


/* 
    a while loop is a pre-test loop in that it tests before execution. In this case, a = 4, the loop tests to see if a < 3, it is false, therefor the body is not executed.
*/
    while (a < 3) {
        System.out.println(a);
        a ++;
    }
/* 
    a do-while loop is a post-test loop in that it runs the body first, then tests for continuation. in this case, the output is 5, even though the test case is false.
*/
    do {
        System.out.println(b);
        b ++;
    } while (b < 3);
/*
    setting both variables back to 
 */
  }
}
