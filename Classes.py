

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

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

emp_1 = Employee('Corey','Tugns',50000)
emp_2 = Employee('Test','User',60000)

# print(emp_1.email)
# print(emp_2.email)



# print(emp_2.fullname())

# print(Employee.fullname(emp_1))

# print(emp_1.pay)
emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(Employee.num_of_employees)
