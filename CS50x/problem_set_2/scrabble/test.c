#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    string new;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        string new += toupper(s[i]);
    }
    printf("After: %s", new);
    printf("\n");
}
