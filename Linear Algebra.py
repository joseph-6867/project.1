import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("\nAddition:\n", A + B)

print("\nSubtraction:\n", A - B)

print("\nMultiplication:\n", np.dot(A, B))

print("\nTranspose of A:\n", A.T)

print("\nDeterminant of A:", np.linalg.det(A))

print("\nInverse of A:\n", np.linalg.inv(A))


np.random.seed(42)

print("\nRandom number:", np.random.rand())

print("\nRandom 2x3 array:\n", np.random.rand(2, 3))

print("\nRandom integers:\n", np.random.randint(1, 10, size=(2, 2)))

# Normal distribution
print("\nNormal distribution values:\n", np.random.randn(3))
