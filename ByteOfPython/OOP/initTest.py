# __init__ 方法相当于类class的初始化方法，可以在初始化方法中做一些操作

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('My name is:', self.name)


p = Person('Jack')

p.say_hi()