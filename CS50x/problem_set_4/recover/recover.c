#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

bool check(BYTE test[512]);

int main(int argc, char *argv[])
{
    // Check whether argc is equal to 2
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    // Open file and return 1 if it is unsuccessful
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    // initialize an int to record the jpeg file number
    int i = 0;

    // a buffer array to store the 512 byte
    BYTE buffer[512];
    char filename[8];
    FILE *img = NULL;
    while (fread(buffer, 512, 1, card) != 0)
    {
        // Check whether it is header of new jpeg
        if (check(buffer) == true)
            // If it is first jpeg
            if (img == NULL)
            {
                sprintf(filename, "%03i.jpg", i);
                img = fopen(filename, "w");
                fwrite(buffer, 512, 1, img);
            }

            // If one is currently open
            else
            {
                fclose(img);
                i++;
                sprintf(filename, "%03i.jpg", i);
                img = fopen(filename, "w");
                fwrite(buffer, 512, 1, img);
            }

        // If not header of jpeg
        else
            // if one is currently open
            if (img != NULL)
            {
                fwrite(buffer, 512, 1, img);
            }

            // if no jpeg file opened
            else
            {
                continue;
            }
    }
    fclose(img);
    fclose(card);
}

bool check(BYTE test[512])
{
    if ((test[0] == 0xff) && (test[1] == 0xd8) && (test[2] == 0xff) && ((test[3] & 0xf0) == 0xe0))
        return true;
    else
        return false;
}
