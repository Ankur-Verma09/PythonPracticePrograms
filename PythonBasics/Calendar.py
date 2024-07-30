import calendar


class Calendar:
    @staticmethod
    def display_calendar():
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))

        cal = calendar.month(year, month)
        print(cal)

    display_calendar()