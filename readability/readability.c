#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // input for text
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    // fomula for finding grade
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

// Print Grade level compared to index
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}


// FUNCTION TO LOOP THROUGH LETTERS IN TEXT
int count_letters(string text)
{
    int letters = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    int words = 1;

    for (int w = 0; w < strlen(text); w++)
    {
        if (isspace(text[w]))
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;

    for (int s = 0; s < strlen(text); s++)
    {
        if (text[s] == 33 || text[s] == 46 || text[s] == 63)
        {
            sentences++;
        }
    }
    return sentences;
}