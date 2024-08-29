#include <cs50.h>
#include <stdio.h>

int check_sum(long card_number);
void valid_check(long card_number, int digit_sum);

int main(void)
{
    // Prompt the user for the credit card number
    long card_number = get_long("Input: ");
    valid_check(card_number, check_sum(card_number));
}

int check_sum(long card_number)
{
    long temp_card = card_number;
    int card_length = 0;
    while (temp_card > 0)
    {
        temp_card /= 10;
        card_length += 1;
    }
    printf("card length: %i\n", card_length);
    int sum_of_digit = 0;
    while (card_number > 0)
    {
        // Get the last digit and add to the sum
        int temp_digit1 = card_number % 10;
        sum_of_digit += temp_digit1;
        card_number = card_number / 10;

        // Get the second last digit, multiply by two and add to sum
        int temp_digit2 = card_number % 10 * 2;
        if (temp_digit2 >= 10)
        {
            int quotient = temp_digit2 / 10;
            int remainder = temp_digit2 % 10;
            sum_of_digit += quotient;
            sum_of_digit += remainder;
        }
        else if (temp_digit2 < 10)
        {
            sum_of_digit += temp_digit2;
        }
        card_number = card_number / 10;
    }
    printf("sum of digit: %i\n", sum_of_digit);
    return sum_of_digit;
}

void valid_check(long card_number, int digit_sum)
{
    long temp_card = card_number;
    //Get card length
    int card_length = 0;
    while (temp_card > 0)
    {
        temp_card /= 10;
        card_length += 1;
    }
    temp_card = card_number;
    //Check the digit sum and the card length to see which credit card it matches
    if ((digit_sum % 10 == 0) && (card_length <= 16))
    {
        temp_card = card_number;
        while (temp_card > 100)
        {
            temp_card /= 10;
        }
        printf("starting digit: %li\n", temp_card);
        if ((temp_card == 34 || temp_card == 37) && card_length == 15)
        {
            printf("AMEX\n");
        }
        else if ((temp_card >= 51 && temp_card <= 55) && card_length == 16)
        {
            printf("MASTERCARD\n");
        }
        else if ((temp_card >= 40 && temp_card <= 49) && (card_length == 13 || card_length == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
