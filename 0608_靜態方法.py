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

    @staticmethod
    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

    @staticmethod #靜態方法裝飾後實際上跟類沒什麼關係,把它當作一個單純的函數
    def eat1(self):
        print("%s is eating %s" % (self.name, 'food'))

    @staticmethod  # 靜態方法裝飾後實際上跟類沒什麼關係,把它當作一個單純的函數
    def eat2(self):
        print("%s is eating %s" % (self.name, 'food'))


d = Dog1("旺財")

# d.eat("寶錄")
# d.eat1() #一般呼叫函數 不丟東西給他 但是會缺少self
d.eat2(d) #但是丟對象的話,就可以順利使用self.name
