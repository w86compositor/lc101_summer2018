# """Returns True if string is sorted from least to greatest
#    False otherwise.
# """
# TODO: Fill in details
# return False


def is_sorted(string):
    return all(string[i] <= string[i+1] for i in range(len(string)-1))


print(is_sorted("ABC"))  # == True
print(is_sorted("aBc"))  # == False
print(is_sorted("dog"))  # == False


# phrase = 'Before you go to bed, you need to brush your teeth.'
# # print(phrase.find(','))

# list = ''

# for letter in phrase:
#     if letter == ',':
#         list += letter + len(phrase)

# print(list)
