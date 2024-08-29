from cs50 import get_string


def main():
    # Prompt user for text
    text = get_string("Text: ")
    letters = 0
    words = 1
    sentences = 0
    punctuation = ["!", ".", "?"]

    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        elif text[i] == " ":
            words += 1
        elif text[i] in punctuation:
            sentences += 1
    grade = round(0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8)
    if grade > 16:
        print("Grade 16+")
    elif (1 > grade):
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

    print(f"letters = {letters}")
    print(f"words = {words}")
    print(f"sentences = {sentences}")


main()
