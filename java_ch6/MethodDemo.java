public class MethodDemo {
    public static int max1(int num1, int num2) {
        int result;
    
        if (num1 > num2)
            result = num1;
        else
            result = num2;
    
        return result;
    }
    public static int max2(int num1, int num2) {
        if (num1 > num2)
            return num1;
        else
            return num2;
    }
    public static int max3(int num1, int num2) {
        return (num1 > num2) ? num1 : num2;
    }
	public static int sum(int i1, int i2) {
	  int result = 0; 
	  for (int i = i1; i <= i2; i++) 
		result += i; 
		
	  return result; 
	}
	  
	public static void main(String[] args) { 
	  System.out.println("Sum from 1 to 10 is " + sum(1, 10)); 
	  System.out.println("Sum from 20 to 37 is " + sum(20, 37));
	  System.out.println("Sum from 35 to 49 is " + sum(35, 49)); 
      System.out.println("Sum from 1 to 10 is " + max1(1, 10)); 
	  System.out.println("Sum from 20 to 37 is " + max1(20, 37));
	  System.out.println("Sum from 35 to 49 is " + max1(35, 49)); 
      System.out.println("Sum from 1 to 10 is " + max2(1, 10)); 
	  System.out.println("Sum from 20 to 37 is " + max2(20, 37));
	  System.out.println("Sum from 35 to 49 is " + max2(35, 49)); 
	}
}

// modifier returnValueType methodName(list of parameters) {
    // Method body;
// }

// modifier - a java keyword that specifies the properties of data, methods, and classes and how they can be used. Examples are public, private, and static.

// returnValueType is the data type the method returns. Methods that don't return a value are called void | value-returning method or void method

// java method = python function