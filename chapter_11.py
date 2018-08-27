def sort_contacts(contacts):
    result = []
    for fkey in sorted(contacts):
        result.append(
            (fkey, contacts[fkey][0], contacts[fkey][1]))
    return result


print(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
                     "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}))
# Should return this:
# 'Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'
# 'Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com'
