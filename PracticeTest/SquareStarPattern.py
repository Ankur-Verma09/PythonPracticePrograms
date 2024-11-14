class SquareStarPattern:
    n = int(input('Enter your value: '))
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()
