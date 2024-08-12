import numpy as np
import math

class ArrayUsingNumpy:
    @staticmethod
    def define1Darray():
        a = np.array([1,2,3])
        print(a)
        print(a.shape)

    @staticmethod
    def twoDarray():
        b = np.array([[1,2,3],[4,5,6]])
        print(b)
        print(b.size)
        print(len(b))
        print(b.shape)

    @staticmethod
    def sumarray():
        a = np.array([1,2,3])
        b = np.array([4,5,6])
        print(np.sum([a,b]))

    @staticmethod
    def sum_of_array_by_row():
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(np.sum([a,b], axis=0))

    @staticmethod
    def sum_of_array_by_column():
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(np.sum([a, b], axis=1))

    @staticmethod
    def sub_array():
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(np.subtract(a,b))

    @staticmethod
    def mul_array():
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(np.multiply(b, a))

    @staticmethod
    def divide_array():
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        print(np.divide(b, a))

    @staticmethod
    def exponential_array():
        a = np.array([1,2,3,4])
        print(np.exp(a))

    @staticmethod
    def power_on_array():
        a = np.array([1, 2, 3, 4])
        print(np.power(a,2))

    @staticmethod
    def sqrt_on_array():
        a = np.array([1, 2, 3, 4])
        print(np.sqrt(a))

    @staticmethod
    def sin_on_array():
        print(np.sin(30* 3.14/180))

    @staticmethod
    def cos_on_array():
        print(np.sin(30 * math.pi / 180))

    @staticmethod
    def aggrigate_functions_in_array():
        a = np.array([1, 2, 3, 4, 5, 6])
        print('sum ', str(np.sum(a)))
        print('Max value ', str(np.min(a)))
        print('Min value ', str(np.max(a)))
        print('Median value ', str(np.median(a)))
        print('standard deviation ', str(np.std(a)))

    @staticmethod
    def compair_array():
        a = [1,2,3]
        b = [2,4,4]
        c = [1,2,4]
        print(np.equal(a,b))
        print(np.array_equal(a,c))

    @staticmethod
    def compair_element_in_array():
        a = np.array([[1,2],[3,4]])
        b = np.array([[1,3],[2,4]])
        c = np.array([[1,2],[3,4]])
        print(np.equal(a,b))
        print(np.equal(a,c))

    @staticmethod
    def v_stack():
        a = [1, 2, 3]
        b = [2, 4, 4]
        print(np.vstack([a,b]))


    @staticmethod
    def h_stack():
        a = [1, 2, 3]
        b = [2, 4, 4]
        print(np.hstack([a, b]))

    @staticmethod
    def initialize_array_with_all_zeros():
        print(np.zeros([3,4]))

    @staticmethod
    def initialize_array_with_a_particular():
        print(np.full([3, 4],10))

    @staticmethod
    def indexing():
        a = np.zeros([3,4])
        print(a)
        a[1][2] = 3.14
        print(a)

    indexing()


