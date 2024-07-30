class AreaOfTriangle:
    @staticmethod
    def area_of_triangle():
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print("Area of Triangle: ", area)

    area_of_triangle()