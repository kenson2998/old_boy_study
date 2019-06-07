class People:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        self.friends = []

    def argue(self):
        print("%s 很生氣" % self.Name)


class Relation(object):
    '''
    左右順序繼承的關係
    Man先繼承 Relation會報錯,因為沒有Name屬性
    Woman先繼承People,所以print(self.Name) 不會報錯
    '''

    # def __init__(self, n1, n2):
    #     print(self.Name, n1, n2)

    def make_friend(self, obj):
        print("%s 和 %s 成為朋友" % (self.Name, obj.Name))
        self.friends.append(obj)
        self.friends.append(obj.Name)


class Man(Relation, People):
    def __init__(self, *args):
        super(Man, self).__init__(args[0], args[1])
        self.Money = args[2]
        print("%s 一出生就有 %s money. " % (self.Name, self.Money))

    def play(self):
        print('%s is man正在玩～' % self.Name)


class Woman(People, Relation):
    def __init__(self, *args):
        super(Woman, self).__init__(args[0], args[1])
        self.Money = args[2]
        print("%s 一出生就有 %s money. " % (self.Name, self.Money))

    def sleep(self):
        People.argue(self)
        print('我是%s is man在睡覺～' % self.Name)


m1 = Man('Leon', 22, 5000)

w2 = Woman('Leona', 40, 1000)

m1.make_friend(w2)
w2.make_friend(m1)

print(w2.friends, "    obj.Name字串傳入的方式: %s , obj位址的方式append才會跟著改名字: %s" %(w2.friends[1], w2.friends[0].Name))

m1.Name = 'Rod'  # 如果m1改名的話, 就會跟著改變,所以self.friends.append(obj) 這邊才會傳obj的方式而不是傳obj.Name
print("m1.Name = 'Rod' 改名字")
print(w2.friends, "    obj.Name字串傳入的方式: %s , obj位址的方式append才會跟著改名字: %s" %(w2.friends[1], w2.friends[0].Name))
