math = input("Expression: ")
x, y, z = math.split(" ")

if y == "+":
    an = float(x) + float(z)
    print(f"{an}")
elif y == "-":
    an = float(x) - float(z)
    print(an)
elif y == "/":
    an = float(x) / float(z)
    print(an)
elif y == "*":
    an = float(x) * float(z)
    print(an)