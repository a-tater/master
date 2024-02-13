#include <stdio.h>
#include <stdbool.h>

int main() {

/*
int = integers
float = floating point numbers (Decimals)
char = signel characters 'a', 'B' - surrounded by single quotes
boolean = true or false | 1 or 0

Syntax
type variableName = value

*/

    int one = 1;
    int twentySeven = 27;
    float thirtyPointFour = 30.4;
    char lowercaseM = 'm';
    bool taterRocks = true;

/*
Print Variables
%d = int
%f = float
%c = char
*/

    printf("%d\n", one); // outputs variable one with value 1
    printf("%f\n", thirtyPointFour); // outputs float 30.4
    printf("%c\n", lowercaseM); // outputs char 'm'
    printf("The boolean 'taterRocks' returns 'true' or %d\n", taterRocks);

    printf("Placeholders can be used to print the integer 1 with %d", one);
    printf("\nMultiple variables %f and newlines \ncan be incorporated using the printf function \n \n%c", thirtyPointFour, lowercaseM);


//Adding Variables
    int four = 4;
    int five = four + one;
    printf("\n%d", five);

//Declaring multiple variables
    int x = 5, y = 2, z = 8;
    int v = x + y + z;
    printf("\n%d", x + y + z + v);

/*
Naming Conventions

variables must start with letter or underscore _
names can contain letters, numbers, and underscores
names are case sensitive
names cannon contain whitespaces or special characters
reserved words cannot be used as names
*/


    return 0;
}