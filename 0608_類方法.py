#    @staticmethod 靜態方法 不常使用

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


D = Dog("旺財")

D.eat("寶錄")


class Dog1(object):
    name = '華仔'
    n = 333

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating %s" % (self.n, 'ddd'))


d = Dog1("旺財")
d.eat()


class Foo:
    '''描述這個類Foo是做什麼用的'''
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("%s running the call" % self.name, args, kwargs)
    def talk(self):
        print("talk")


print("印出Foo的描述說明：", Foo.__doc__)
b = Foo("BBBB")
a = Foo("AAAA")()
b()
b(1,2,3,name=123)
print("class.__dict__:",Foo.__dict__) #打印類裡的所有屬性,不包含實例屬性
print("b.__dict__:",b.__dict__) #只顯示實際產生的屬性,不包含類屬性


from lib_0609.aa import C

c = C()

print("module:", c.__module__)  # 輸出模塊
print("class:", c.__class__)  # 輸出類

print(c)

