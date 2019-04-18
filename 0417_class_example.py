class dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print('%s:旺旺叫！' % self.name)


d1 = dog('陳龍華')
d2 = dog('陳四')
d3 = dog('陳三砲')

d1.bulk()
d2.bulk()
d3.bulk()


class role:
    def __init__(self, name, role, weapon, life_value=100, money=10000):  # 生命和金錢已給個默認值,可寫可不寫
        # __init__ 叫做構造函數
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print('%s use %s shooting...' % (self.name, self.weapon))

    def got_shot(self):
        self.life_value -= 10
        print('%s:I got shot. HP:%d' % (self.name, self.life_value))

    def buy_gun(self, gun_name):
        print('I buy : %s' % gun_name)
        self.weapon = gun_name


r1 = role('Leon', 'police', 'b43')  # 創建一個角色

r1.shot()
r1.got_shot()
r1.got_shot()
r1.buy_gun('B51')
r1.shot()

# 上述的 r1 = role('Leon', 'Police', 'b43')
# 其實是 role(r1, 'Leon', 'Police', 'b43') ,把r1帶入到role()裡面了