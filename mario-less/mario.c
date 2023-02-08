#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Block input
    int n, i, j, s;
    do
    {
        n = get_int("Width: ");
    }
    while (n > 8 || n <= 0);

    // Height of block
    for (i = 0; i < n; i++)
    {
        // Spaces
        for (s = 0; s < n - i - 1; s++)
        {
            printf(" ");
        }

        // Row of block
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}