import numpy as np
a1 = np.arange(10)
a2 = np.arange(10, 20).reshape(2, 5)
a3 = np.arange(20, 28).reshape(2, 2, 2)

print(a1)
print(a2)
print(a3)

print(a1[0:6:2])
print(a2[0, :])
print(a2[:,1])
print(a2[0,1 ])
print(a2[1, 1:4:2])
print(a2[ 1:4:2,1])
