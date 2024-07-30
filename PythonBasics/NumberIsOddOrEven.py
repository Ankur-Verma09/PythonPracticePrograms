class NumberIsOddOrEven:
    @staticmethod
    def off_or_even():
        num = int(input('Enter a number: '))
        if num % 2 == 0:
            print('Number is even')
        else:
            print('Number is odd')

    off_or_even()