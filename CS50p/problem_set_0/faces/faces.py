def main():
    question = input("What would you like to say?")
    convert = question.replace(":)","🙂").replace(":(","🙁")
    print(convert)

main()

