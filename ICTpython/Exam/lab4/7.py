n = int(input())
word = input().lower()
set = set(word)
if len(set) == 26:
    print('YES')
else:
    print('NO')
