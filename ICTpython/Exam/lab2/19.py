n = int(input())
a = map(int, input().split())
c = []
k = 0
for i in a:
    c.append(i)
for i in range(len(c)-1):
    for j in range(i+1, len(c)):
        if c[i] == c[j]:
            k += 1

print(k)
