import math

n = int(input())
fib = int((((1 + (5)**0.5) ** n) - ((1 - (5)**0.5) ** n)) / ((2 ** n) * (5)**0.5))
print(fib)
