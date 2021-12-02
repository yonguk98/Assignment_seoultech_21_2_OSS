import numpy as np

'''A = np.array([3,29,82])
print(A)
print(A.T)
print(np.array_equal(A,A.T))
E = np.array([[3],[29],[82]])
print(E)
print(E.T)
print(A.T == E.T)

F = np.zeros((3,2))
H = np.eye(3)
I = np.empty((3,2))
J = np.empty((0,9))
M = np.random.uniform(size = (3,2))
print(F ,'\n', H ,'\n', I ,'\n', J ,'\n', M)'''

A = np.array([[1,2],[3,4]])
det = np.linalg.det(A)
print(f"{det}")

print(A + [[1],[1]])