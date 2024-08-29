user_input = input("Input:")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
print("Output: ", end="")
for i in user_input:
    if i in vowels:
        #or just use continue here, skipping to the next iteration
        i.replace(i,"")
    else:
        print (i, end="")
print()

