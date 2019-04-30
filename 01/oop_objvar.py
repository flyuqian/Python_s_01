class Robot:
    """表示有一个带有名字的机器人"""

    population = 0

    def __init__(self, name):
        ''' 初始化数据 '''
        self.name = name
        print('Initializing {}'.format(self.name))

        Robot.population += 1

    def die(self):
        '''我挂了'''
        print('{} is being destroyed'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(Robot.population))


    def say_hi(self):
        ''' 来自机器人的惩治问候

        没问题, 你做得到 '''
        print('Greetings, my master call me {}.'.format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前机器人的数量"""
        print('we have {:d} robots.'.format(cls.population))


print(Robot.__doc__)
droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C2-P0')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here\n')
print('Robots have finished their work, so lets destroy them')
droid1.die()
droid2.die()

Robot.how_many()
