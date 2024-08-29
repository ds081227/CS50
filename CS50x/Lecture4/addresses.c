#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("Pointer: %p\n", &s);
    printf("Address of string[0]: %p\n", &s[0]);
    printf("Address of string[1]:%p\n", &s[1]);
    printf("Address of string[2]:%p\n", &s[2]);
    printf("Address of string[3]:%p\n", &s[3]);
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));
}
