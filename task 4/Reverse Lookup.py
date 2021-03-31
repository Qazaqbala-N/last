def reverseLookUp(s, v):
    keys = []
    for i, j in s.items():
        if j == v:
            keys.append(i)
    return keys
dict1 = {'A':18, 'Aaa':17, 'bbb':18,'Acc':22}
print(reverseLookUp(dict1, 16))
print(reverseLookUp(dict1, 17))
print(reverseLookUp(dict1, 18))
print(reverseLookUp(dict1, 22))
