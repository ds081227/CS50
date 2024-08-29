#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickles(int cents);
int calculate_pennies(int cents);

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int quarters;
    quarters = calculate_quarters(cents);
    cents = cents - (quarters * 25);

    int dimes;
    dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10);

    int nickles;
    nickles = calculate_nickles(cents);
    cents = cents - (nickles * 5);

    int pennies;
    pennies = calculate_pennies(cents);
    cents = cents - pennies;

    int coins;
    coins = quarters + dimes + nickles + pennies ;
    printf("%i",coins);
    printf("\n");

}

int calculate_quarters(int cents)
{
    int quotient = cents / 25;

    return quotient;
}

int calculate_dimes(int cents)
{
    int quotient = cents / 10;
    return quotient;
}

int calculate_nickles(int cents)
{
    int quotient = cents / 5;
    return quotient;
}

int calculate_pennies(int cents)
{
    int quotient = cents / 1;
    return quotient;
}

