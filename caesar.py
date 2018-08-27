from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    foo = list(text)
    finalValue = []
    for f in foo:
        finalValue.append(rotate_character(f, rot))
    return "".join(finalValue)


def main():
    a = input("Type a message: ")
    b = input("Rotate by: ")
    print(encrypt(a, int(b)))


if __name__ == "__main__":
    main()
