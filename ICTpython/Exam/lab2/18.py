n = int(input())
a = map(int, input().split())
c = []
for i in a:
    c.append(i)
temp = c[0]
for i in range(n - 1):
    c[i] = c[i + 1]
c[n - 1] = temp
print(c)
