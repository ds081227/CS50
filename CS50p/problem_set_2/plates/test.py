# import string library function
import string

# Storing the sets of punctuation in variable result
result = string.punctuation

# Printing the punctuation values
print(result)


def ends_with(string):
    if string.isalpha():
        return True
    elif string.isalnum():
        if string[2:6].isnumeric():
            if string.endswith("0123456789"):
                return True
        elif string.endswith("123456789"):
            return True

elif string.isalnum():
        if string[3:5].isnumeric():
            if string[-1].isnumeric():
                return True
        elif string.endswith("1","2","3","4","5","6","7","8","9"):
                return True

number_list_with_0 = ["0123456789"]
number_list_without_0 = ["123456789"]
if  start_letters(s) and max_count(s) and punctuation_check(s) and position(s) and ends_with(s) and zero_check(s)

def position(s):
    if s.alnum():
        for i in s:
            if i.isalpha():
                return index(i)
def ends_with(s):
    if s.isalpha():
        return True
    elif s.isalnum():
        if i.isnumeric():
            if s[[i]:-1].isnumeric():
                return True
            else:
                return False
