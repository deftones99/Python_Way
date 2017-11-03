# coding= UTF-8

class schoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print('初始化schoolMember :{}'.format(self.name))

    def tell(self):
        print('name:{},age:{}'.format(self.name, self.age), end=',')


class teacher(schoolMember):
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary
        print('初始化teacher:{}'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('Salary:{:d}'.format(self.salary))


class student(schoolMember):
    def __init__(self, name, age, mark):
        schoolMember.__init__(self, name, age)
        self.mark = mark
        print('初始化student:{}'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('Mark:{:d}'.format(self.mark))


t = teacher('Jack', 42, 50000)
s = student('Rose', 23, 90)

print()

members = [t, s]
for member in members:
    member.tell()

print(help(str))