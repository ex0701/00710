import numpy as np
from numpy.linalg import inv,det
v1 = np.array([1,2,3])
m1 = np.array([[1,2],[3,4]])
v2 = np.array([4,5,6])
m2 = np.array([[5,6],[7,8]])

print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")

#Addition
a1 = v1+v2
print("Vector:",a1)
a2 = m1+m2
print("Matrix: ")
print(a2)

#Subtraction
s1 = v2-v1
print("Vector:",s1)
s2 = m2-m1
print("Matrix:")
print(s2)

#Dot Product
d1 = np.dot(v1,v2)
d2 = np.dot(m1,m2)
print("Vector:",d1)
print("Matrix:")
print(d2)

#Transpose
t1 = m1.T
print("Transpose of Matrix")
print(t1)

#Inverse
inv1 = inv(m1)
print(inv1)

#Determinant
det1 = det(m1)
print(det1)
