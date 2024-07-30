class NumberStatus:

    @staticmethod
    def if_number_is_positive():
        num = float(input('Enter an number: '))
        if num < 0:
            print('Number is negative')
        elif num == 0:
            print('Number is Zero')
        else:
            print('Nunber is positive')

    if_number_is_positive()