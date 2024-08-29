import string
punctuation_list = string.punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if  start_letters(s) and max_count(s) and punctuation_check(s) and ends_with(s) and zero_check(s):
        return True
    else:
        return False
#start with at least two letters
def start_letters(s):
    if s[0:2].isalpha():
        return True
#contain maximum of 6characters(letters or numbers),minimum of 2 characters
def max_count(s):
    if  6 >= len(s) >= 2:
        return True
#no periods, spaces or punctuation marks
def punctuation_check(s):
    for i in s:
        if i in string.punctuation:
            return False
    return True
#number cannot be in the middle of plate
def ends_with(s):
    if s.isalpha():
        return True
    for i in s:
        if i.isdigit():
            index = s.index(i)
            if s[index:].isdigit():
                return True
            else:
                return False
#first number used cannot be 0 using for loop
def zero_check(s):
    if s.isalpha():
        return True
    for i in s:
        if i.isnumeric():
            if i == "0":
                return False
            else:
                return True
#first number used cannot be 0 using index
def zero_check1(s):
    if s.isalpha():
        return True
    elif s.isalnum():
        if s[s.find("0") - 1].isalpha():
            return False
        else:
            return True

if __name__ == "__main__":
    main()

