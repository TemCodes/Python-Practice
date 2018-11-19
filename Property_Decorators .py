class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property             #This allows us to access this method as an attribute
    def email(self):
        return(self.first + '.' + self.last + '@company.com')

    @property             #This allows us to access this method as an attribute
    def fullname(self):
        return(self.first + ' ' + self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')



emp_1.fullname = 'Corey Bakster'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
