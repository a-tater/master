#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("\n");
    //Loops execute a block of code as long as a specified condition is reached

/*While Loop
    while (condition) {
        //code block to be executed
    };
*/

    int i = 0;

    while (i < 5) {
        printf("%d\n", i + 1);
        i ++;
    };
    printf("the end\n\n");

/*
Do While
The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.
*/

    int y = 0;

    do {
        printf("%d\n", y + 1);
        y++;
    }
    while (y < 5); // runs code 5 times


    do {
        printf("%d\n", y + 1);
        y++;
    }
    while (y < 5); // runs code one time, evaluates to false, stops running

    printf("\n\n");


// For Loops

    return 0;
}