import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figlet = figlet.getFonts()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Error")

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet:
        word = input("Input: ")
        font = sys.argv[2]
        cust = Figlet(font=font)
        print((cust.renderText(f"{word}")))
    else:
        sys.exit("Error")

elif len(sys.argv) == 1:
    word = input("Input: ")
    randomf = random.choice(figlet)
    cust = Figlet(font = randomf)
    print(cust.renderText(f"{word}"))

else:
    sys.exit("Error")
