def main():
    answer = unmodified_answer(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
    if answer == "42" or answer =="forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
def unmodified_answer(a):
    return str(a.lower().strip())
main()