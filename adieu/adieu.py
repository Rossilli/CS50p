names = []
while True:
    try:
        name = input("Enter a name: ")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
    print("Adieu, adieu, to " + names[0])
elif len(names) == 2:
    print("Adieu, adieu, to " + ' and '.join(names))
else:
    print("Adieu, adieu, to " + ', '.join(names[:-1]) + ", and " + names[-1])
