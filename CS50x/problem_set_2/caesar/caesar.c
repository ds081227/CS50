#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int digit_check(string test);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    if ((argc == 2) && (digit_check(argv[1]) == 0))
    {
        // Convert key from string to int
        int key = atoi(argv[1]);
        while (key > 26)
        {
            key -= 26;
        }
        key %= 26;
        printf("The key is %i\n", key);
        // Prompt user for text
        string plain_text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, n = strlen(plain_text); i < n; i++)
        {
            printf("%c", rotate(plain_text[i], key));
        }
        printf("\n");

        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

int digit_check(string test)
{
    for (int i = 0, n = strlen(test); i < n; i++)
    {
        if (!isdigit(test[i]) || (test[i] < 0))
        {
            return 1;
        }
    }
    return 0;
}

char rotate(char c, int n)
{
    if (isalpha(c))
    {
        if (isupper(c))
        {
            c = (c - 65 + n) % 26 + 65;
            return c;
        }
        else if (islower(c))
        {
            c = (c - 97 + n) % 26 + 97;
            return c;
        }
    }
    return c;
}
