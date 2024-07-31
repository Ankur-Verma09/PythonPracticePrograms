class LeapYear:
    @staticmethod
    def validate_leap_year():
        year = int(input('Enter year: '))
        if(year % 400 == 0) and (year % 100 == 0):
            print(year ,' is leap year')
        elif (year % 4 == 0) and (year % 100 != 0):
            print(year, ' is leap year')
        else:
            print(year, ' is not leap year')

    validate_leap_year()