word = str(input())

lowerC = 0
upperC = 0
for i in word:
    if i.isupper():
        upperC += 1
    elif i.islower():
        lowerC += 1

if upperC > lowerC:
    word = word.upper()
else:
    word = word.lower()

print(word)