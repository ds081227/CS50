#include <cs50.h>
#include <stdio.h>
#include <string.h>

int collatz(int n);
int counter = 0;
int main(void)
{
    //do something
    int number = get_int("What is n? ");
    collatz(number);
    printf("It took %i steps.\n", counter);
}

int collatz(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if (n % 2 == 0)
    {
        counter++;
        return collatz(n / 2);
    }
    else
    {
        counter++;
        return collatz(3 * n + 1);
    }
}
