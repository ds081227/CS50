import inflect
p = inflect.engine()
name_list = []
try:
    while True:
        name_input = input("Name: ")
        name_list.append(name_input)
except EOFError:
        print()
        print("Adieu, adieu, to", p.join(name_list))
