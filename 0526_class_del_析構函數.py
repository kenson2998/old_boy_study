# 用於實例釋放或銷毀的時候自動執行的,通常用於做一些收尾工作,如關閉一些數據庫鏈接、打開的臨時文件


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('%s 徹底死了...' % self.name)

    def say(self, saything):
        print('%s say %s' % (self.name, saything))


MAN = Person('Leon')
MAN.say('eo4')
MAN1 = Person('peter')
MAN1.say('eo4')


# __del__ 一定是最後才做的


class Person1:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('%s 完了...' % self.name)

    def say(self, saything):
        print('%s say %s' % (self.name, saything))


MAN2 = Person1('noce')
MAN2.say('eo4')
del MAN2  # 如果先del 就會優先做__del__
MAN3 = Person1('axv')
MAN3.say('eo4')
