class SumOfNaturalNumber:
    @staticmethod
    def sum_of_natural_num():
        sum = 0
        limit = int(input('Enter the value: '))
        for i in range(1, limit + 1):
            sum += i

        print('Sum of natural number up to ', limit, ' is: ', sum)

    sum_of_natural_num()