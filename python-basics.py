
# some python basics

# for i in range(1, 11):
#     print i

# i = 1
# while i <= 10:
# 	print i
# 	i += 1

# a = 10
# b = 20
# if a < b:
# 	print "{} is less than {}".format(a, b)
# elif a == 20:
# 	print "{} is equal to {}".format(a, b)
# else:
# 	print "{} is greater than {}".format(a, b)


import sys
print(sys.executable)
print(sys.version)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
