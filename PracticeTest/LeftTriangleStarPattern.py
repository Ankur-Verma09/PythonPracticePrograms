class LeftTriangleStarPattern:
    n = int(input('Enter any number: '))
    # for i in range(1, n):
    #     for j in range(n, 0, -1):
    #         if j>i:
    #             print(' ', end='')
    #         else:
    #             print('*', end= '')
    #     print()

    for i in range(n):
        for j in range(n-i):
            print('', end=' ')
        for k in range(0, i+1):
            print('*', end='')
        print()