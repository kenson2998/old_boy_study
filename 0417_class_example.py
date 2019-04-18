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
    n = 123  # 這是類變量
    name = "我是類name"
    n_list = []

    def __init__(self, name, role, weapon, life_value=100, money=10000):  # 生命和金錢已給個默認值,可寫可不寫
        # __init__ 叫做構造函數
        # 在實例化時做一些類的初始化的工作
        self.name = name  # 實例變量(靜態屬性),作用域就是實例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):  # 類的方法, 功能(動態屬性)
        print('%s use %s shooting...' % (self.name, self.weapon))

    def got_shot(self):
        self.life_value -= 10
        print('%s:I got shot. HP:%d' % (self.name, self.life_value))

    def buy_gun(self, gun_name):
        print('I buy : %s' % gun_name)
        self.weapon = gun_name


r1 = role('Leon', 'police', 'b43')  # 創建一個角色
r2 = role('Jack', 'terrorist', 'b41')  # 創建一個角色

r1.shot()
r1.got_shot()
r1.got_shot()
r1.buy_gun('B51')
r1.shot()
r1.bullet_prove = True  # 沒有的變數也可以在這邊生成
# del r1.weapon # 也可以刪除

r1.n = '456'  # 修改r1的n
print(r1.n, r1.name, r1.bullet_prove, r1.weapon)
print(r2.n, r2.name, r2.weapon)

role.n = '修改n'  # 直接改class裡面的n
print('r1.n: %s, r2.n: %s' % (r1.n, r2.n))

r2.n_list.append('from r2')  # 但是list裡面如果修改, 對所有的都會一起修改

print('role.n_list: %s, r1.n_list: %s, r2.n_list: %s' % (role.n_list, r1.n_list, r2.n_list))

# 上述的 r1 = role('Leon', 'Police', 'b43')
# 其實是 role(r1, 'Leon', 'Police', 'b43') ,把r1帶入到role()裡面了
