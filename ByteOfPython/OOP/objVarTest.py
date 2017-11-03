class Robot:
    '''表示有一个带有名字的机器人'''

    population = 0# 类变量

    def __init__(self, name):
        self.name = name # name属于某个对象，因此是对象变量
        print('Initializing {}'.format(self.name))

        Robot.population += 1

    def die(self):
        print('{} is die'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} is the last one robot'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(Robot.population))

    def say_hi(self):
        print('你好，我叫{}'.format(self.name))

    @classmethod
    def how_many(cls):
        print('We had {:d} robots'.format(cls.population))


droid1 = Robot('RD-1')
droid1.say_hi()
print(Robot.population)
Robot.how_many()

droid2 = Robot('RD-2')
droid2.say_hi()
print(Robot.population)
Robot.how_many()

print('Destory Robots')

droid1.die()
droid2.die()

Robot.how_many()