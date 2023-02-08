def main():
    twt = input("Input: ")
    voweless = shorten(twt)
    print(voweless)

def shorten(tw):
    rmv = ("aeiouAEIOU")
    for x in rmv:
        tw = tw.replace(x, "")
    return tw


if __name__ == "__main__":
    main()