#    @staticmethod 靜態方法 不常使用

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


D = Dog("旺財")

D.eat("寶錄")


class Dog1(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self, food):
        print("%s is eating %s" % (self.name, food))



d = Dog1("旺財")
d.eat()