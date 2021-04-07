import math

t1, g1 = map(int, (input().split()))
t2, g2 = map(int, (input().split()))
print(6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)))
