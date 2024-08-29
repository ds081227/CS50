#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int argc_check(int argc);
int key_check(string key);
int length_check(string key);
int repeat_check(string key);
string cipher(string plain_text, string key);

int main(int argc, string argv[])
{
    if ((argc_check(argc) == 0) && (length_check(argv[1]) == 0) && (key_check(argv[1]) == 0) && (repeat_check(argv[1]) == 0))
    {
        string key = argv[1];
        // Prompt user for text
        string plain_text = get_string("plaintext: ");
        string cipher_text = cipher(plain_text, key);
        printf("ciphertext: %s\n", cipher_text);
        free(cipher_text);
        return 0;
    }
    else
    {
        return 1;
    }
}

// Check the length of argc
int argc_check(int argc)
{
    if (argc == 2)
    {
        return 0;
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}

// Check whether there are invalid keys
int key_check(string key)
{
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
    }
    return 0;
}

// check whether key has 26 characters
int length_check(string key)
{
    if (strlen(key) == 26)
    {
        return 0;
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}

// Check whether there are repeated keys
int repeat_check(string key)
{
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if ((i != j) && (key[i] == key[j]))
            {
                printf("Keys must not contain repeated characters.\n");
                return 1;
            }
        }
    }
    return 0;
}

// Pass in plain text and return the ciphered text
string cipher(string plain_text, string key)
{
    int n = strlen(plain_text);
    char *cipher_text = malloc((n + 1) * sizeof(char));
    for (int i = 0; i < n; i++)
    {
        if (isalpha(plain_text[i]))
        {
            if (isupper(plain_text[i]))
            {
                int position = plain_text[i] - 65;
                cipher_text[i] = toupper(key[position]);
            }
            else if (islower(plain_text[i]))
            {
                int position = plain_text[i] - 97;
                cipher_text[i] = tolower(key[position]);
            }
        }
        else
        {
            cipher_text[i] = plain_text[i];
        }
    }
    cipher_text[n] = '\0';
    return cipher_text;
}
