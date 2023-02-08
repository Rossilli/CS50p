#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string text);
char rotate(char c, int n);

int main(int argc, string argv[])
{
        // 1 COMMAND LINE INPUT
        int k, length;
        string plaintext;

        if (argc != 2 || !only_digits(argv[1]))
        {
            printf("Usage: %s key\n", argv[0]);

            return 1;
        }
        // LOOP TEXT AND SWITCH
        k = atoi(argv[1]);
        plaintext = get_string("plaintext: ");
        length = strlen(plaintext);
        char ciphertext[length + 1];
        for (int i = 0; i < length; i++)
        {
            ciphertext[i] = rotate(plaintext[i],k);
        }
        printf("ciphertext: %s\n", ciphertext);

        return 0;
}






    // DIGIT ONLY FALSE IF NOT
bool only_digits(string text)
{
    for (int k = 0; k < strlen(text); k++)

    if (!isdigit(text[k]))
    {
        return false;
    }

    return true;
}
    // ROTATE CHAR
char rotate(char p, int k)
{
    char ci, pi, c = 0;

    if (isupper(p))
    {
        pi = p - 65;
        ci = (pi + k) % 26;
        c = ci + 65;
    }
    else if (islower(p))
    {
        pi = p - 97;
        ci = (pi + k) % 26;
        c = ci + 97;
    }
    else
    {
        return p;
    }
    return c;
}

