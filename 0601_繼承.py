class People:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def eat(self):
        print('%s 正在吃東西～' % self.Name)
    def sleep(self):
        print('%s 正在睡覺～' % self.Name)
    def jump(self):
        print('%s 正在跳～' % self.Name)

class Man(People):
    def play(self):
        print('%s 正在玩～' % self.Name)

m1 = Man('Leon',22)

m1.eat()
m1.play()