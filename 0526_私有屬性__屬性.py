class Person:
    def __init__(self, name):
        self.name = name
        self.__life_value = 100  # 私有屬性

    def got_shot(self):
        print('中槍 -50HP')
        self.__life_value -= 50

    def show_status(self):
        print('HP : %s' % self.__life_value)

    def __shot(self):  # 私有方法
        print('%s 開槍' % self.name)


MAN = Person('Leon')

print('顯示名字:', MAN.name)
# print('顯示血量:', MAN.__life_value) # 變成無法訪問的私有屬性了
MAN.got_shot()

MAN.show_status()
# MAN.__shot()# 變成無法訪問的私有方法了