class ArithmeticOperations:
    @staticmethod
    def addition():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sum_result = num1 + num2
        print("Sum of the numbers is: ", sum_result)

    @staticmethod
    def multiplication():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        multi_result = num1 * num2
        print("Multiplication of numbers: ", multi_result)

    @staticmethod
    def division():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        division_result = num1/num2
        print("Result of division: ", division_result)

    @staticmethod
    def substraction():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sub_result = num1 - num2
        print("Result of substraction: ", sub_result)
