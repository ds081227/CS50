from pyfiglet import Figlet
figlet = Figlet()
import sys
from random import choice
fontlist = figlet.getFonts()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fontlist:
        user_input = input("Input: ")
        font_input = sys.argv[2]
        f = figlet.setFont(font = font_input)
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    user_input = input("Input: ")
    font_input = choice(fontlist)
    f = figlet.setFont(font = font_input)
    print(figlet.renderText(user_input))

else:
    sys.exit("Invalid usage")



