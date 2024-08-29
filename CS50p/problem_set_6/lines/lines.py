import sys
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                line_number = 0
                for line in file:
                    if line.isspace() or line.lstrip().startswith("#"):
                        continue
                    else:
                        line_number += 1
                print(line_number)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file")




