class MultiplicationTable:

    @staticmethod
    def table():
        num = int(input('Enter number for table: '))
        for i in range(1, 11):
            print(num, 'X', i, '=', (num*i))

    table()