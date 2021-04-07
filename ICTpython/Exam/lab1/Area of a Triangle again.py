import math

s1, s2, s3 = map(int, (input().split()))
s = s1 + s2 + s3
print("Area :" + str(((s) * (s - s1) * (s - s2) * (s - s3)) ** 0.5))
