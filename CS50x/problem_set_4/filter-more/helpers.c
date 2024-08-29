#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row of height
    for (int i = 0; i < height; i++)
    {
        // Iterate over each pixel in the row
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            image[i][j].rgbtRed = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, l = width - 1; j < width / 2; j++, l--)
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
    // Create an array for copy
    RGBTRIPLE copy[height][width];
    // Copying the original image to this new array for calculations
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // Using the copy to calculate the correct RGB for blur
    for (int i = 0; i < height; i++) // row
    {
        for (int j = 0; j < width; j++) // column
        {
            float red = 0, green = 0, blue = 0, counter = 0;
            for (int k = 1; k > -2; k--) // row
            {
                for (int l = 1; l > -2; l--) // column
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Create an array for copy
    RGBTRIPLE copy[height][width];
    // Copying the original image to this new array for calculations
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // Create a two-dimensional array of Gx and Gy
    float Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    float Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    for (int i = 0; i < height; i++) // row
    {
        for (int j = 0; j < width; j++) // column
        {
            float GxRed = 0, GxGreen = 0, GxBlue = 0, GyRed = 0, GyGreen = 0, GyBlue = 0;
            for (int k = -1; k < 2; k++) // row
            {
                for (int l = -1; l < 2; l++) // column
                {
                    if ((i + k >= 0) && (j + l >= 0) && (i + k < height) && (j + l < width))
                    {
                        GxRed += copy[i + k][j + l].rgbtRed * Gx[k + 1][l + 1];
                        GxGreen += copy[i + k][j + l].rgbtGreen * Gx[k + 1][l + 1];
                        GxBlue += copy[i + k][j + l].rgbtBlue * Gx[k + 1][l + 1];
                        GyRed += copy[i + k][j + l].rgbtRed * Gy[k + 1][l + 1];
                        GyGreen += copy[i + k][j + l].rgbtGreen * Gy[k + 1][l + 1];
                        GyBlue += copy[i + k][j + l].rgbtBlue * Gy[k + 1][l + 1];
                        float channel[3];
                        // Red
                        channel[0] = sqrt(GxRed * GxRed + GyRed * GyRed);
                        // Green
                        channel[1] = sqrt(GxGreen * GxGreen + GyGreen * GyGreen);
                        // Blue
                        channel[2] = sqrt(GxBlue * GxBlue + GyBlue * GyBlue);
                        for (int m = 0; m < 3; m++)
                            if (channel[m] > 255)
                                channel[m] = 255;
                        image[i][j].rgbtRed = round(channel[0]);
                        image[i][j].rgbtGreen = round(channel[1]);
                        image[i][j].rgbtBlue = round(channel[2]);
                    }
                }
            }
        }
    }

    return;
}

