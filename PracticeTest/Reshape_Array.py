import numpy as np

class Reshape_Array:

    @staticmethod
    def reshape():
        array = np.array([[1,2,3,4,5],[2,5,4,6,7]])
        print(array)
        new_arr = array.reshape(5,2)
        print(new_arr)

    reshape()