n = int(input())
a = []

k = map(int, input().split())
a.append(k)
r = 0
for i in range(len(a)):
    if min(a) <= a[i] <= max(a):
        r += 1

print(max(a) - min(a)+1 - r)
