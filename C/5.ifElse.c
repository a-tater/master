#include <stdio.h>
#include <stdbool.h>

int main() {

/*
            If / Else
if - specifies a block of code is to be executed if specified condition evaluates to true
else - specifies a block of code to be executed if the same condition evaluates to false
else if - specifies a new condition to test if the first condition evaluates to false
switch - specifies an alternative block of code to be executed
*/


    bool taterRocks = true;
    int five = 5;
    int ten = 10;

    if (taterRocks) {
        printf("%d\n", five < ten);
    };


    if (five > 10) {
        printf("the world has gone to shit\n");
    } else {
        printf("tater rocks! %d\n", taterRocks);
    };


    if (five > ten) {
        printf("the world has gone to shit\n");
    } else if (five < ten) {
        if (taterRocks) {
            printf("tater rocks!\n");
        } else {
            printf("the world really does suck\nbut at least i'm using line breaks!\n");
        }
    } else {
        printf("this isn't very good code\n");
    };

//Shorthand if / else:
//       if                      then                             else
    (five > ten) ? printf("five is greater than ten") : printf("this is pretty nifty\n\n");

    return 0;
}