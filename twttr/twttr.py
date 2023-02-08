def main():
    twt = input("Input: ")
    voweless = vowel(twt)
    print(voweless)

def vowel(tw):
    rmv = ("aeiouAEIOU")
    for x in rmv:
        tw = tw.replace(x, "")
    return tw

main()