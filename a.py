def get_initials(fullname):
    fullNameList = fullname.split()
    print(fullNameList)
    collection = []
    for i in fullNameList:
        collection += i[0:1].capitalize()
    initials = ''.join(collection)
    return initials


def main():
    print(get_initials("Daniel Day Lewis"))


if __name__ == '__main__':
    main()
