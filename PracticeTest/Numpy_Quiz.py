import numpy as np

class Numpy_Quiz:

    def bub_sort(array):
        for i in range(0, len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] < array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j+1] = temp
            print(array)
            return array
    my_array = np.array([20,14,25,16,45,60,12,9])


    @staticmethod
    def select_element_and_create_array():
        arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
        print(arr[0:3,1])

    @staticmethod
    def horizontally_stack():
        Array1 = np.arange(20, 2)
        print(f'Array1 is: {Array1}')
        Array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        new_arr = np.hstack((Array1, Array2))
        print(new_arr)

    @staticmethod
    def stack_array():
        array1 = np.array([[1,2],[3,4]])
        array2 = np.array([[5,6],[7,8]])
        new_arr = np.stack((array1,array2))
        print(new_arr)

    @staticmethod
    def cross_product_of_vectors():
        A = np.array([[4],[12],[29]])
        print(A)
        B = np.array([[13],[21],[4]])
        new_arr = np.cross(A,B)
        print(new_arr)

    @staticmethod
    def correlation_coefficient():
        A = np.array([1,3,5,7,9,11,13,15,17,19,21,23,25])
        B = np.array([0,2,4,6,8,10,12,14,16,18,20, 22, 24])
        result = np.corrcoef(A,B)
        print(result)

    @staticmethod
    def nested_array():
        sample = {1: [1,2],
                  2: [[1],[2]],
                  3: [[1,2], [3,4], [4,5]],
                  4: [1],
                  5: [1,2,3,4,5]}
        result = sample.values()
        data = list(result)
        numpyArr = np.array(data, dtype=object)
        print(numpyArr)

    @staticmethod
    def find_number_of_element():
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
        print(arr.size)
        print(np.size(arr))

    @staticmethod
    def code_output():
        list = [3, 9, 12, 15]
        a = (x ** 3 for x in list)
        print(next(a))

    @staticmethod
    def index_value():
        array = np.arange(13,23, 4)
        print("Sequence:", array)
        try:
            index_of_17th = np.where(array == 17)
            print(index_of_17th)
        except IndexError:
            print('No element found')

    index_value()

