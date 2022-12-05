class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay
        
    # added additional formtting to first and last name

        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def createEmail(self):
        return '{}'.format(self.first.lower() + '.' + self.last.lower() + '@home.com')
    # added additional formatting to email gen

    # class function/method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class Developer(Employee)
    #   pass

    # Adding new line of code to see if it works
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('nIK', 'Stojkov', 20000) # testing formtting with incorrectly inserted data
emp_2 = Employee('Anna', 'Hollebon', 30000)

print(emp_1.createEmail())
print(emp_1.fullName())
