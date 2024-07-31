class HCM:
    @staticmethod
    def find_hcm(x, y):
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        return  hcf

    num1 = int(input('Enter the number: '))
    num2 = int(input('Enter the number: '))

    print('The H.C.F. is ', find_hcm(num1, num2))