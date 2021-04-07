import numpy as np
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]] ])
print(b[1,0,1])
b[:,1,:] = [[-1,-2],[-8,-8]]
print(b)