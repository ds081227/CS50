def main():
    user_input = input("Input:")
    output_list = shorten(user_input)
    newstring = ''.join(output_list)
    print(newstring)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = ""
    for i in word:
        if i in vowels:
            continue
        else:
            output += i
    return output

if __name__ == "__main__":
    main()

