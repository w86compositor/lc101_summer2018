LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encryptMessage(key, message):
    return translateMessage(key, message)


def translateMessage(key, message):
    translated = []  # Stores the encrypted/decrypted message string.

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
            num += LETTERS.find(key[keyIndex])  # Add if encrypting.
        num %= len(LETTERS)  # Handle any wraparound.

        # Add the encrypted/decrypted symbol to the end of translated:
        if symbol.isupper():
            translated.append(LETTERS[num])
        elif symbol.islower():
            translated.append(LETTERS[num].lower())

        keyIndex += 1  # Move to the next letter in the key.
        if keyIndex == len(key):
            keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting:
            translated.append(symbol)

    return ''.join(translated)


print(encryptMessage("boom", "The crow flies at midnight!"))
