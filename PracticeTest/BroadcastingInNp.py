import numpy as np

def broadcasting():
    a= np.array([[0,0,0],[1,2,3],[4,5,6],[5,6,7]])
    b= np.array([[0,1,2]])
    print("First array: \n", a, '\n')
    print("Second array: \n", b, '\n')
    print("First array + Second array: \n", a+b, '\n')


broadcasting()