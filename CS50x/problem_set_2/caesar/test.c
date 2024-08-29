#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int integer = get_int("Number: ");
    while (integer > 26)
    {
        integer -= 26;
    }
    printf("Integer is %i \n", integer);
    int remainder = integer % 26;
    printf("Remainder is %i \n", remainder);
}
