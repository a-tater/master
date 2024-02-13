#include <stdio.h>

int main() {

/*
Basic Data Types and Format Specifiers
Name    Format      Size            Notes
int     %d or %i    2 or 4 bytes    
float   %f or %F    4 bytes         can store 6-7 decimal digits
double  %lf         8 bytes         can store 15 decimal digits
char    %c          1 byte          stores single ASCII value
string  %s

floats & doubles can be stored as scientific number
*/
    float  m = 35e3; // = 35 * (10 * 3) = 35000
    double z = 12E4; // = 12 * (10 * 4) = 120000
    printf("%f\n", m); // default is six decimal places
    printf("%lf\n", z); //default is six decimal places


//Set Decimal Precision
    printf("%.1f\n", m); //sets one decimal place
    printf("%.4lf\n", z); //sets four decimal places


/*
sizeof operator to get size of variable
%lu is Format for printf function
*/

    printf("The size of the 'float' variable 'm' is %lu bytes\n", sizeof(m));
    printf("The size of the 'double' variable 'z' is %lu bytes\n", sizeof(z));


/*
Type Conversion

Implicit Conversion (automatic)
Explicit Conversion (manual)
*/

    int five = 5;
    int two = 2;

    int sum = five / two; // returns 2
    int sums = 5 / 2; // returns 2

    printf("%d\n", sum);
    printf("%d\n", sums);

    //Implicit Conversion
    float myFloat = 9; // returns 9.000000
    int myInt = 9.9999; // returns 9
    float mySum = 5 / 2; // returns 2.0000

    //Explicit Conversion
    float mySum2 = (float) 5 / 2; // returns 2.50

    printf("%f\n", myFloat);
    printf("%d\n", myInt);
    printf("%f\n", mySum);
    printf("%.2f\n", mySum2);


    //Constants
    //Declaring a variable a constant makes it unchangeable and read-only

    const int myVar = 15;
    // int myVar = 10; // this produces an error

    //Constants must be created with a value

    const int milesPerHour = 60; // this will work
    // const int milesPerSecond;
    // milesPerSecond = 60; // this will not work



    return 0;
}