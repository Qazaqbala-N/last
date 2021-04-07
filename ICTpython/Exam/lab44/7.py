dictionary = dict()
s = input()

for i in range(32, 127):
    dictionary[chr(i)] = 0
count = 0
for i in range(0, len(s)):
    if dictionary.get(s[i]) != None:
        if dictionary[s[i]] != 1 and dictionary[s[i]] != 2:
            dictionary[s[i]] = 1
            count += 1
        else:
            dictionary[s[i]] = 2
print(count)
