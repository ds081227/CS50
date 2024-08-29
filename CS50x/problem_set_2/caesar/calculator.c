#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    int z = x / y;
    int remainder = x % y;
    printf("quotient is %i",z);
    printf("\n");
    printf("remainder is %i",remainder);
    printf("\n");
}

