class RightTriangleStarPattern:
    n = int(input("Enter number: "))
    for i in range(n):
        for j in range(i):
            print('*', end=' ')
        print()