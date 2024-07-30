from PythonBasics import Employee

class Person():
    def __init__(self, eid, fname, sname, salary, dob, gender, addr, uid):
        Employee.__init__(self, eid, fname, sname, salary)
        self.per_dob = dob
        self.per_gender = gender
        self.per_addr = addr
        self.per_uid = uid



per1 = Person(104, 'Neha', 'Singh', 20000, '11-09-1999', 'Female', 'Bangalore', 12345)

