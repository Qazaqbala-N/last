n = int(input())
print(n % 10 + int(n / 10 % 10) + int(n / 100 % 10) + int(n / 1000 % 10))
