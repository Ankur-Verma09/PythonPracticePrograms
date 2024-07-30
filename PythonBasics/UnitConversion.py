class UnitConversion:
    @staticmethod
    def km_to_miles_converter():
        kilometers = float(input("Enter the distance in kilometer: "))
        conversion_factor = 0.621371
        miles = kilometers * conversion_factor
        print("Distance in miles is: ", miles)
    @staticmethod
    def cel_to_f():
        celsius = float(input('Enter temperature in celsius: '))
        fahrenheit = (celsius *9/5) +32
        print('Temprature in Fahrenheit is: ', fahrenheit)

    cel_to_f()