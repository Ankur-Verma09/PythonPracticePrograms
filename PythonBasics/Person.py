from Employee import Employee

class Person():
    def __init__(self, eid, fname, sname, salary, dob, gender, addr, uid):
        Employee.__init__(self, eid, fname, sname, salary)
        self.per_dob = dob
        self.per_gender = gender
        self.per_addr = addr
        self.per_uid = uid

    def get_dob(self):
        return self.per_dob

    def get_gender(self):
        return self.per_gender

    def get_addr(self):
        return self.per_addr

    def get_uid(self):
        return self.per_uid


per1 = Person(104, 'Neha', 'Singh', 20000, '11-09-1999', 'Female', 'Bangalore', 12345)

