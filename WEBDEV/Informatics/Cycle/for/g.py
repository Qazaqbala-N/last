import math
a = int(input())

print(([str(math.gcd(i,a)) for i in range(2,a+1) if math.gcd(a,i) != 1])[0])