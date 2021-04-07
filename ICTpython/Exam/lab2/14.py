k = int(input())
r = 0
s = 0
a = [1]
while k != 0:
    k = int(input())
    if s == k:
        a.append(k)
    if k > s:
        s = k
print(len(a))
