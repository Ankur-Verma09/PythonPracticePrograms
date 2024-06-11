import numpy as np

def initnpArray():
    print(np.zeros((3,4)))

# arranging the numbers b/wx and y with an interval z
def initinpArrayWithInterval():
    print(np.arange(1,10,2))

# enev number b/w 10 and 20
def initinpArrayWithInterval1():
    print(np.arange(10,20,2))


# arrange z numbers b/s x and y
def arrangeNumberWithZintervals():
    # print(np.linspace(5,10,10))
    print(np.linspace(0,10,6))


# Filling same number in an array of dimension x and Y
def sameNumberInArray():
    print(np.full((2,3),6))

# Filling random number in an array of dimension x and Y
def randomNumberInArray():
    print(np.random.random((2,3)))

# initnpArray()
# initinpArrayWithInterval()
# initinpArrayWithInterval1()
# arrangeNumberWithZintervals()
# sameNumberInArray()
randomNumberInArray()