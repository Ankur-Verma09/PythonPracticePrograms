import numpy as np

# Check size of teh array
def inspectArray():
    a=np.array([[2,3,4],[4,5,6]])
    s=np.array([[2,3,4,5],[4,5,6,7],[7,8,9,0]])
    print((a.shape))
    print((s.shape))

def reziseArray():
    a = np.array([[2, 3, 4], [4, 5, 6]])
    # trick: x*y = Total number of elemts in the array
    a.shape = (3,2)
    print(a)


# Check dimention of the arraay
def demOfArr():
    a = np.arange(24)
    print(a.ndim)
    # trick: Calculate the factor of 24: 1,2,3,6,8,12,24
    b=a.reshape(12,2)
    print(b)
    print(b.ndim)

# Number of elements in an array
def elemOfArray():
    a= np.array([[1,2,3],[1,2,4]])
    print(a.size)

# Find datatype of an array
def dataTyoeOfArray():
    # a=np.arange(24)
    a = np.arange(24, dtype=float)
    print(a.dtype)
    print(a)


# inspectArray()
# reziseArray()
# demOfArr()
# elemOfArray()
dataTyoeOfArray()