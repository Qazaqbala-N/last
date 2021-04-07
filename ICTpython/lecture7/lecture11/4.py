import numpy as np
v1 = np.array([1,2,3,4,5])
v2 = np.array([6,7,8,9,0])
a = np.vstack([v1,v2,v1,v2,v1])
print(a)
print(a[:2,3:])

print(a[2:4,0:2])