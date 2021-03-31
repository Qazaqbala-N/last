n = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = 0
b = 0
for i in arr:
    if i > a:
        b = a
        a = i
print(b)
