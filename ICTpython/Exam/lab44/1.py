dictionary = dict()


def reverse_Lookup(val, diction):
    list = []
    for i, j in diction.items():
        if j == val:
            list.append(i)
    return list


Countries = ['Russia', 'France', 'USA', 'Japan', 'Kazakhstan']

for i in Countries:
    if len(i) % 2 == 0:
        dictionary[i] = 0
    else:
        dictionary[i] = 1
# print(dictionary.items())
print(reverse_Lookup(0, dictionary))
