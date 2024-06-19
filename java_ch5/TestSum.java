public class TestSum {
    public static void main(String[] args) {
      // Initialize sum
      float sum = 0;
  
      // Add 0.01, 0.02, ..., 0.99, 1 to sum
      for (float i = 0.01f; i <= 1.0f; i = i + 0.01f)
        sum += i;
  
      // Display result
      System.out.println("The sum is " + sum);

      // Initialize sum
      double sum1 = 0;
  
      // Add 0.01, 0.02, ..., 0.99, 1 to sum
      for (double i = 0.01f; i <= 1.0f; i = i + 0.01f)
        sum1 += i;
  
      // Display result
      System.out.println("The sum is " + sum1);


      // Initialize sum
      double currentValue = 0.01;
      double sum2 = 0;
  
      // Add 0.01, 0.02, ..., 0.99, 1 to sum
      for (int count = 0; count < 100; count++) {
        sum2 += currentValue;
        currentValue += 0.01;     
      }
  
      // Display result
      System.out.println("The sum is " + sum2);


    }
  }