class SwapTwoNumbers:
    @staticmethod
    def swap_without_third_variable():
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        a = a + b
        b = a - b
        a = a - b

        print('After swap a value is: ', a)
        print('After swap b value is :', b)

    @staticmethod
    def swap_with_third_variable():
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        temp = a
        a = b
        b = temp

        print('After swap a value is: ', a)
        print('After swap b value is :', b)

    swap_with_third_variable()
