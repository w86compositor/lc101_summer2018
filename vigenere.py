from helpers import alphabet_position, rotate_character


def encrypt(text, keyword):
    result = ""

    for x, letter in enumerate(text):
        if text[x].isalpha():
            # DO THIS
            # for x, letter in enumerate(text):
            key_pos = alphabet_position(keyword[x % len(keyword)])
            result += rotate_character(letter, key_pos)
            print(f"key_pos inside if: {key_pos}")
        else:
            # DO THAT
            # return result + letter
            result += letter
            print(f"key_pos if else statement is executed: {key_pos}")

    return result


def main():
    a = input("Type a message: ")
    b = input("Encryption key: ")
    print(encrypt(a, b))


if __name__ == "__main__":
    main()


#vigenere.encrypt('BaRFoo', 'BaZ')
#vigenere.encrypt('The crow flies at midnight!', 'boom')
#'Uvs osck rmwse bh auebwsih!'
