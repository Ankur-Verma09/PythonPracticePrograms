import numpy as np

def concatenateArray():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.concatenate((a,b)))

# Stack array row-wise: vertically
def concatenateArrayVer():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.vstack((a,b)))

# Stack array row-wise: Horizontaly
def concatenateArrayHor():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.hstack((a,b)))

# Stack array column wise
def concatenateArrayCol():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.column_stack((a,b)))


# Slipt array
def splitArray():
    a = np.arange(16).reshape(4,4)
    print(a)
    # print("\n\n", np.hsplit(a,2))
    # print("\n\n", np.hsplit(a,np.array([3,6])))
    print("\n\n", np.hsplit(a, np.array([3])))
    print("\n\n", np.hsplit(a, np.array([2,3])))


# concatenateArray()
# concatenateArrayVer()
# concatenateArrayHor()
# concatenateArrayCol()
splitArray()
