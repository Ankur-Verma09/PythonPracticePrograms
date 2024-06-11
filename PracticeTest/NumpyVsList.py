import numpy as np
import sys
import time

def compairMemory():
    l= range(1000)
    print("Size of a list: ", sys.getsizeof(1)*len(l))
    a = np.arange(1000)
    print("Size of a array: ", a.size*a.itemsize)

def using_List():
    t1 = time.time() # initial time
    X= range(10000)
    Y= range(10000)
    z = [X[i]+Y[i] for i in range(len(X))]
    return  time.time()-t1

def using_Numpy():
    t = time.time()
    a = np.array(10000)
    b = np.array(10000)
    z = a+b
    return time.time()-t

list_time = using_List()
numpy_time = using_Numpy()

print(list_time,numpy_time)
print("In this example numpy is " +str(list_time / numpy_time)+ "times faster than a list")

# compairMemory()
using_List()
using_Numpy()