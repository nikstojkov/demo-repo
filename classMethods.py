class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay

        Employee.num_of_emps += 1

    def FullName(self):
        return '{} {}'.format(self.first, self.last)
    def CreateEmail(self):
        return '{}'.format(self.first + '.' + self.last + '@home.com')
   #class function/method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#class Developer(Employee)
 #   pass

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Nik', 'Stojkov', 20000)
emp_2 = Employee('Anna', 'Hollebon', 30000)

print(emp_1.CreateEmail())
