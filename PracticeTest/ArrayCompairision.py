import numpy as np

# Element wise compairision
def compairArray():
    a = np.array([1, 2, 4])
    b = np.array([2, 4, 4])
    c = np.array([1, 2, 4])
    print(np.equal(a,b))
    print(np.equal(a, c))


# Array wise compairision
def compairArrayWise():
    a = np.array([1, 2, 4])
    b = np.array([2, 4, 4])
    c = np.array([1, 2, 4])
    print(np.array_equal(a,b))
    print(np.array_equal(a, c))

compairArrayWise()