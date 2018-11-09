

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

emp_1 = Employee('Corey','Tugns',50000)
emp_2 = Employee('Test','User',60000)

print(Employee.raise_amnt)
print(emp_1.raise_amnt)
print(emp_2.raise_amnt)

Employee.set_raise_amt(1.05) #update the class method, we are working with the class and not the instance

print(Employee.raise_amnt)
print(emp_1.raise_amnt)
print(emp_2.raise_amnt)


#I keep getting strings and need to parse them
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1)

##### Static Practice
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
