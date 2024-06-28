import java.util.Scanner;

public class Exercize08_21 {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter the number of cities: ");
    int numberOfCities = input.nextInt();

    double[][] cities = new double[numberOfCities][2];
    System.out.print("Enter the coordinates of the cities: ");
    for (int i = 0; i < cities.length; i++) {
      cities[i][0] = input.nextDouble();
      cities[i][1] = input.nextDouble();
    }

    double p1 = 0, p2 = 1;
    double shortestDistance = -1;
    
    double distance;
    double[] base = new double[2];
    for (int i = 0; i < cities.length; i++) {
      distance = 0;
      base[0] = cities[i][0];
      base[1] = cities[i][1];
      for (int j = 0; j < cities.length; j++) {
        distance += distance(cities[i][0], cities[i][1],
          cities[j][0], cities[j][1]);
      }
      if ((shortestDistance > distance) ^ (shortestDistance < 0)) {
        p1 = cities[i][0];
        p2 = cities[i][1];
        shortestDistance = distance;
        }
    }
    System.out.println("The central city is at (" + p1 + ", " + p2 + ")");
    System.out.println("The total distance to all other cities is " + shortestDistance);
  }

  public static double distance(double x1, double y1, double x2, double y2) {
    return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
  }
}