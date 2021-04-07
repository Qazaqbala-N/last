n = int(input())
a = []
for i in range(1, n+1):
    n = int(input())
    a.append(n)
b = set(a)
print(len(b))