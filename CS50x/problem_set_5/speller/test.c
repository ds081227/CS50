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
