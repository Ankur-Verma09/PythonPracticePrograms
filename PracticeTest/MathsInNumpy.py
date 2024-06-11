import numpy as np

def sumOfTwoNum():
    sum = np.sum([10,20])
    print(sum)

def sumOfTwoNumWithParm(a,b):
    sum = np.sum([a,b])
    print(sum)

def sumOf2DArray():
    # a= np.sum([[1,2],[5,6]], axis=0) #adding x axis array
    # a = np.sum([[1, 2], [5, 6]], axis=1) #adding y axis array
    a = np.sum([[1, 2], [5, 6]]) #adding all element of array
    print(a)

def subTwoNum():
    sub = np.subtract(10, 20)
    print(sub)

def mulTwoNum():
    mul = np.multiply(10, 20)
    print(mul)

def divTwoNum():
    div = np.divide(10, 20)
    print(div)

def divOf2DArray():
    a = np.array([2, 2])
    b = np.array([4, 6])
    print(np.divide(a,b))

def mulOf2DArray():
    a = np.array([2, 2])
    b = np.array([4, 6])
    print(np.multiply(a,b))

def expOfArray():
    a = np.array([2, 2])
    b = np.array([4, 6])
    print(np.exp(a))

def sqrtOfArray():
    a = np.array([2, 2])
    b = np.array([4, 6])
    print(np.sqrt(a))

def sinOfArray():
    a = np.array([90, 2])
    b = np.array([4, 6])
    print(np.sin(a))

def cospOfArray():
    a = np.array([2, 2])
    b = np.array([4, 6])
    print(np.cos(a))

def logOfArray():
    a = np.array([90, 2])
    b = np.array([4, 6])
    print(np.log(a))

# Aggrigate of Function
def aggrigateOfArray():
    a = np.array([1, 2, 4])
    b = np.array([2, 4, 4])
    c = np.array([1, 2, 4])
    print("Sum: ", np.sum(a))
    print("min value of array: ", np.min(a))
    print("mean value of array: ", np.mean(a))
    print("median value of array: ", np.median(a))
    print("coorelation coefficient value of array: ", np.corrcoef(a))
    print("standard daviation value of array: ", np.std(a))

# sumOfTwoNum()
# sumOfTwoNumWithParm(10,20)
# sumOf2DArray()
# subTwoNum()
# mulTwoNum()
# divTwoNum()
# divOf2DArray()
# mulOf2DArray()
# expOfArray()
# sqrtOfArray()
# sinOfArray()
# cospOfArray()
# logOfArray()
aggrigateOfArray()