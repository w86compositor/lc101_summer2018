import string
b = string.ascii_lowercase


def alphabet_position(letter):
    return b.find(letter.lower())


def rotate_character(char, rot):
    if isinstance(char, str) and char.isalpha() and len(char) == 1 and isinstance(rot, int):
        value = alphabet_position(char) + rot
        if value < 26:
            for count_1, d in enumerate(b):
                if value == count_1:
                    return d.upper() if char.isupper() else d
        elif value >= 26:
            greaterValue = value % 26
            for count_2, e in enumerate(b):
                if greaterValue == count_2:
                    return e.upper() if char.isupper() else e
    else:
        return char
