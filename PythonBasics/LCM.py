class LCM:
    @staticmethod
    def find_LCM(x, y):
        if x > y :
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
    num1 = int(input('Enter the number: '))
    num2 = int(input('Enter the number: '))

    print('The L.C.M. is ', find_LCM(num1, num2))

