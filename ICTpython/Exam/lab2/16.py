k = int(input())
a = []
a.append(k)
while k != 0:
    k = int(input())
    a.append(k)
c = []
for i in range(1, len(a)):
    if i+1 != len(a) and a[i] > max(a[i - 1], a[i + 1]):
        c.append(a[i])
print(len(c))
