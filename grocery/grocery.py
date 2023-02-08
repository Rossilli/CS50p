def main():
    glist = {}

    while True:
        try:
            grocery = input("").upper()
            if grocery.upper() in glist:
                glist[grocery.upper()] += 1
            else:
                glist[grocery.upper()] = 1
        except EOFError:
            print("")
            break

    for grocery, count in sorted(glist.items()):
        print(f"{count} {grocery}")


main()