def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a,b = input().split()

print(power(float(a), float(b)))