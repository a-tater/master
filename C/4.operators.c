#include <stdio.h>

int main() {

    int x = 5;
    int y = 3;

/*
            Arithmatic Operators
Operator    Name        Description         Example     x = 5, y = 3
+           Add         Adds two values     x + y       = 8
-           Subtact     Subtracts           x - y       = 2
*           Multiply    Multiplies          x * y       = 15
/           Division    Divides             x / y       = 1
%           Modulus     Returns remainder   x % y       = 2
++          Increment   Increases by 1      ++x         = 6
--          Decriment   Decreases by 1      --x         = 4
*/
    printf("\nArithmatic Operators\n");
    printf("\t%d + %d = %d\n", x, y, x + y);
    x = 5;
    printf("\t%d - %d = %d\n", x, y, x - y);
    x = 5;
    printf("\t%d * %d = %d\n", x, y, x * y);
    x = 5;
    printf("\t%d / %d = %d\n", x, y, x / y);
    x = 5;
    printf("\t%d modulus %d = %d\n", x, y, x % y);
    x = 5;
    y = 5;
    printf("\t++%d = %d\n", y, ++x);
    x = 5;
    printf("\t--%d = %d\n", y, --x);


/*
            Assignment Operators
Operator    Name        Description     Same As     x = 5
=                       x = 5           x = 5       = 5
+=                      x += 3          x = x + 3   = 8
-=                      x -= 3          x = x - 3   = 2
*=                      x *= 3          x = x * 3   = 15
/=                      x /= 3          x = x / 3   = 1
%=                      x %= 3          x = x % 3   = 2
&=         Bin AND      x &= 3          x = x & 3   = 0101 & 0011  = 0001 = 1
|=         Bin OR       x |= 3          x = x | 3   = 0101 | 0011  = 0111 = 7
^=         Bin XOR      x ^= 3          x = x ^ 3   = 0101 ^ 0011  = 0110 = 6
>>=  Bin Right Shift    x >>= 3         x = x >> 3  = 0101 >> 3    = 0000 = 0
<<=  Bin Left Shift     x <<= 3         x = x << 3  = 0101 << 3    = 0010 1000 = 40
*/
    x = 5;
    y = 5;
    printf("\nAssignment Operators\n");
    printf("\t%d += 3 = %d\n",y, x += 3);
    x = 5;
    printf("\t%d -= 3 = %d\n",y, x -=3);
    x = 5; 
    printf("\t%d *= 3 = %d\n",y, x *= 3);
    x = 5;
    printf("\t%d /= 3 = %d\n",y, x /= 3);
    x = 5;
    printf("\t%d modulo= 3 = %d\n",y, x %= 3);
    x = 5;
    printf("\t%d &= 3 = %d\n",y, x &= 3);
    x = 5;
    printf("\t%d |= 3 = %d\n",y, x |= 3);
    x = 5;
    printf("\t%d ^= 3 = %d\n",y, x ^= 3);
    x = 5;
    printf("\t%d >>= 3 = %d\n",y, x >>= 3);
    x = 5;
    printf("\t%d <<= 3 = %d\n",y, x <<= 3);


/*
            Comparison Operators
Operator    Name                    Example    x = 5
==          Equal to                x == 5     1 = True
!=          Not Eaqual to           x != 5     0 = False
>           Greater than            x > 6      0 = False
<           Less that               x < 6      1 = True
>=          Greater than or = to    x >= 6     0 = False
<=          Less than or = to       x <= 5     1 = True
*/
    x = 5;
    printf("\nComparison Operators\n");
    printf("\t5 == 5 = %d\n", x == 5);
    printf("\t5 != 5 = %d\n", x != 5);
    printf("\t5 > 6 = %d\n", x > 6);
    printf("\t5 < 6 = %d\n", x < 6);
    printf("\t5 >= 6 = %d\n", x >= 6);
    printf("\t5 <= 5 = %d\n", x <= 5);


/*
            Logical Operators
Operator    Name            Example             x = 5
&&          Logical AND     x < 5 && x < 10     0 = False
||          Logical OR      x < 5 || x < 6      1 = True
!           Logical NOT     !(x < 5 || x < 6)   0 = False
*/
    printf("\nLogical Operators\n");
    printf("\t5 < 5 && 5 < 10 = %d\n", x < 5 && x < 10);
    printf("\t5 < 5 || 5 < 6 = %d\n", x < 5 || x < 6);
    printf("\t!(5 < 5 || 5 < 6) = %d\n", !(x < 5 || x < 6));


    return 0;
}