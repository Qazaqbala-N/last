dictionary1 = dict()
dictionary2 = dict()
s1 = input().upper()
s2 = input().upper()

for i in range(65, 91):
    dictionary1[chr(i)] = 0
    dictionary2[chr(i)] = 0
for i in range(0, len(s1)):
    if dictionary1.get(s1[i]) is not None:
        dictionary1[s1[i]] += 1
for i in range(0, len(s2)):
    if dictionary2.get(s2[i]) != None:
        dictionary2[s2[i]] += 1
for i in dictionary1.keys():
    if dictionary1[i] != dictionary2[i]:
        print("They are not anagrams")
        raise SystemExit
print("They are anagrams")
