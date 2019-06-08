class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass

    @staticmethod
    def animal_talk(self,obj):
        obj.talk()

class Cat:
    def __init__(self,name):
        self.Name = name
    def talk(self):
        print("Meow Meow")

class Dog:

    def __init__(self, name):
        self.Name = name

    def talk(self):
        print("woof woof")

def animal_talk(obj): #多態的性質：一個接口
    obj.talk()

c = Cat("貓")
d = Dog("狗")
c.talk()
d.talk()
#一個接口,表現出多重形態
animal_talk(c)
animal_talk(d)
