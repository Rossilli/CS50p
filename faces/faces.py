def main():
    word = input()

    print(convert(word))



def convert(word):

    word = word.replace(":)", "🙂").replace(":(", "🙁")
    return word



main()