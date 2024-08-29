#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //Iterate over each row of height
    for(int i = 0; i < height; i++)
    {
        //Iterate over each pixel in the row
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue ) / 3.0;
            image[i][j].rgbtRed = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        //Iterate over each pixel in the row
        for (int j = 0; j < width; j++)
        {
            int oRed = image[i][j].rgbtRed;
            int oGreen = image[i][j].rgbtGreen;
            int oBlue = image[i][j].rgbtBlue;
            float sepia [3];
            //Sepia Red
            sepia[0] = .393 * oRed + .769 * oGreen + .189 * oBlue;
            //Sepia Green
            sepia[1] = .349 * oRed + .686 * oGreen + .168 * oBlue;
            //Sepia Blue
            sepia[2] = .272 * oRed + .534 * oGreen + .131 * oBlue;
            for (int k = 0; k < 3; k++)
                if (sepia[k] > 255)
                    sepia[k] = 255;
            image[i][j].rgbtRed = round(sepia[0]);
            image[i][j].rgbtGreen = round(sepia[1]);
            image[i][j].rgbtBlue = round(sepia[2]);
        }
    }
    return;
}

// Reflect image horizontally(copying the whole line into an array)
void reflect1(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        RGBTRIPLE copy[width];
        for (int j = 0, w = width - 1; j < width; j++ , w--)
        {
            copy[j] = image[i][w];
        }
        for (int k = 0; k < width; k++)
        {
            image[i][k] = copy[k];
        }
    }
    return;
}

// Reflect image horizontally(swap the first pixel with the last on each row)
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, l = width - 1; j < width / 2; j++ , l--)
        {
            copy = image[i][j];
            image[i][j] = image[i][l];
            image[i][l] = copy;
        }
    }
}



// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Create an array for copy
    RGBTRIPLE copy[height][width];
    //Copying the original image to this new array for calculations
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    //Using the copy to calculate the correct RGB for blur
    for (int i = 0; i < height; i++) //row
    {
        for (int j = 0; j < width; j++) //column
        {
            float red = 0, green = 0, blue = 0, counter = 0;
            for (int k = 1; k > -2; k--) //row
            {
                for (int l = 1; l > -2; l--) //column
                {
                    if ((i - k >= 0) && (j - l >= 0) && (i - k < height) && (j - l < width))
                    {
                        {
                        red += copy[i - k][j - l].rgbtRed;
                        green += copy[i - k][j - l].rgbtGreen;
                        blue += copy[i - k][j - l].rgbtBlue;
                        counter += 1;
                        }
                    }
                }
            }
            image[i][j].rgbtRed = round(red / counter);
            image[i][j].rgbtGreen = round(green / counter);
            image[i][j].rgbtBlue = round(blue / counter);
        }
    }

    return;
}
