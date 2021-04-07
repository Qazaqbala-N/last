n = int(input())
num = 0
for i in range(1, n):
    if n % i == 0:
        num += 1
print(num)
