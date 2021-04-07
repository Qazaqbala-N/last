import math

n = int(input())
a = int(n / 200)
b = int(n % 200 / 100)
c = int(n % 200 % 100 / 25)
d = int(n % 200 % 100 % 25 / 10)
e = int(n % 200 % 100 % 25 % 10 / 5)
f = int(n % 200 % 100 % 25 % 10 % 5)
print("200 :" + str(a) + " 100:" + str(b ) + "  25:" + str(c ) + "  10:" + str(d) + " 5:" + str(e) + "  1:" + str(f))
