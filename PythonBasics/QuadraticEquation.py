import math


class QuadraticEquation:
    @staticmethod
    def quadratic_equation():
        a = float(input('Enter coefficient a: '))
        b = float(input('Enter coefficient b: '))
        c = float(input('Enter coefficient c: '))

        result = b**2 - 4*a*c
        print(result)

        if result >0:
            root1 = (-b + math.sqrt(result)) / (2 * a)
            root2 = (-b - math.sqrt(result)) / (2 * a)
            print('Root 1: ', root1)
            print('Root 2: ', root2)

        elif result == 0:
            root = -b / (2 * a)
            print('Root: ', root)

        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(abs(result)) / (2 * a)
            print('Root 1: ', real_part + imaginary_part)
            print('Root 2: ', real_part - imaginary_part)

    quadratic_equation()