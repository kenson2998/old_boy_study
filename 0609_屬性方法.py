class Dog1(object):
    name = '華仔'
    n = 333

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s" % (self.n, self.__food))

    @eat.setter  # eat傳參數必須要使用setter
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter  # eat想刪除food
    def eat(self):
        del self.__food
        print("del food")


d = Dog1("旺財")
d.eat

d.eat = "包子" #賦值給food
d.eat

del d.eat
d.eat