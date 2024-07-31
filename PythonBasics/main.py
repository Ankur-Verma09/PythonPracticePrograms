from PythonBasics import Person, Tata

class main:
    # @staticmethod
    # def calling_Employee():
    #     object1 = Person.per1
    #     print(object1.per_dob)
    #     print(object1.per_addr)

    @staticmethod
    def calling_car():
        obj = Tata.brand
        print(obj.car_model, obj.company_logo)
        print(obj.get_warrenty())



    calling_car()