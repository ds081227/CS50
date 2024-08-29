#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");
    // Count the number of letters, words, and sentences in the text
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);
    // Compute the Coleman-Liau index
    float index = 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8;
    int grade = round(index);
    // Print the grade level
    if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else if (1 > grade)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    return letters;
}

int count_words(string text)
{
    int words = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (text[i] == 32)
        {
            words += 1;
        }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentences += 1;
        }
    return sentences;
}
