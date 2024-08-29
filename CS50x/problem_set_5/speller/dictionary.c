// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Global variable keeping track of the number of words added in dictionary
unsigned int number_of_words = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word to obtain a hash value
    int index = hash(word);
    // Access linked list at that index in the hash table
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Traverse linked list, looking for the word(strcasecmp)
        if (strcasecmp(word, cursor->word) == 0)
            return true;
        cursor = cursor->next;
    }
    // Return false if no word is found
    return false;
}

// Hashes word to a number(Hashing the first to character of the string)
// N size = 26 * 26
unsigned int hash1(const char *word)
{
    // Value of ALPHA +676(Adding 26 buckets after the 26 * 26 bucket to represent A-Z)
    if (strlen(word) < 2)
    {
        return ((toupper(word[0]) - 'A') * 26 + ((toupper(word[0])) - 'A'));
    }
    // Value of ALPHA * 26 + VALUE of ALPHA
    return ((toupper(word[0]) - 'A') * 26 + ((toupper(word[1])) - 'A'));
}

// Hashes word to a number(Adding the ASCII number of the characters together)
unsigned int hash(const char *word)
{
    int index = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        index += toupper(word[i]) - 'A';
    }
    return index % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Could not open dictionary.\n");
        return false;
    }
    // Creating a word buffer to scanf into
    string word_buffer = malloc(LENGTH + 1);
    if (word_buffer == NULL)
    {
        printf("Failed to allocate memory.\n");
        return false;
    }
    // Read strings from file one at a time
    while (fscanf(dict, "%s", word_buffer) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Failed to allocate memory.\n");
            return false;
        }
        // Copying the word to this node and initialize the address to NULL
        strcpy(n->word, word_buffer);
        n->next = NULL;
        // Hash word to obtain hash value
        int index = hash(n->word);
        // Insert node into hash table at that location
        n->next = table[index];
        table[index] = n;
        // Increase the count of words
        number_of_words++;
    }
    free(word_buffer);
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (number_of_words != 0)
        return number_of_words;
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *temp = NULL;
    node *cursor = NULL;
    for (int i = 0; i < N - 1; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
