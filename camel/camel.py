import re

def main():
    camelstr = input("Camel case: ")
    snakestr = camel_case(camelstr)
    print(snakestr)


def camel_case(camelstr):
    snake_case_string = re.sub(r'([A-Z])', r'_\1', camelstr).lower()
    return snake_case_string

main()