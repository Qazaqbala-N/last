k = int(input())
a, b = 1, 1
while b <= k:
    a = a + 1
    b = b + a * (a + 1) // 2
print(a - 1)

