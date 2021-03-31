a = int(input())
i = 0
s = []
boo = True
while 2**i<=100000000:
    s.append(2**i)
    i = i + 1
for i in range(len(s)):
    if a==int(s[i]):
        print("YES")
        boo =False
if boo:
    print("NO")
