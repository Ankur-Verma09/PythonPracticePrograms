# Develop a system to create and update employee details
# define a class
class Employee:
# constructor function => Used to define and initialize values to the members.
# By default constractor name is __init__
# self => self is not a keyword, it is a variable. It is used to store the reference of the current object.
    def __init__(self, eid, fname, sname, salary):
        self.emp_id = eid
        self.first_name = fname
        self.second_name = sname
        self.emp_sal = salary

    def get_eId(self):
        return self.emp_id

    def get_salary(self):
        return self.emp_sal

    def get_full_name(self):
        return self.first_name + ' ' + self.second_name

    def update_salary(self, increment):
        self.emp_sal = self.emp_sal + increment
        return self.emp_sal

# Object is created/ Class is insantiated => First invokes the constructor
# create an object/instantiate the class
emp1 = Employee(101, 'Elon', 'Musk', 5000)
emp2 = Employee(102, 'John', 'Doe', 1000)
emp3 = Employee(103, 'Alen', 'Verma', 100000)
print(emp1.emp_id, emp1.first_name, emp1.second_name, emp1.emp_sal)
print(emp2.emp_id, emp2.first_name, emp2.second_name, emp2.emp_sal)
print(emp3.emp_id, emp3.first_name, emp3.second_name, emp3.emp_sal)