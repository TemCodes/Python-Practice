

class Employee:

    num_of_employees = 0
    raise_amnt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1  #Def use Employee.num not self.num since this is stays constant for every instance

    def fullname(self):
        return(self.first + ' ' + self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # If we left as Employee.raise_amount we couldnt change the raise amount later on

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amnt = amount   #same as saying Employee.raise_amnt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):       #does not take the instance or the class
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey','Tugns',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1)
print(emp_1 + emp_2)
