class People:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def eat(self):
        print('%s 是人類,正在吃東西～' % self.Name)

    def sleep(self):
        print('%s 是人類,正在睡覺～' % self.Name)

    def jump(self):
        print('%s 是人類,正在跳～' % self.Name)


class Man(People):  # 繼承父親(People)的東西
    def __init__(self, name, age, money):  # 我想要在Man這裡面加上一個money屬性

        '''
        可用 People.__init__(self) 或是 super(Man,self).__init__() 兩種方法
        但super比較方便,因為宣告不用提到父親
        例如：如果Man(People)要改成Man(other)
        People.__init__(self, name, age) 要改成 other.__init__(self, name, age)
        但super宣告不需要修改源碼
        '''

        # People.__init__(self, name, age)  # 調用繼承的People 有name,age屬性 直接self傳自己去套用構造函數就可以了(方法ㄧ)
        super(Man, self).__init__(name, age)  # 調用繼承的People 有name,age屬性 直接self傳自己去套用構造函數就可以了(方法二)

        self.money = money  # 這邊直接宣告money
        print("%s 一出生就有 %s money." % (self.Name, self.money))

    def play(self):
        print('%s is man正在玩～' % self.Name)

    def sleep(self):
        People.sleep(self)
        print('我是%s is man在睡覺～' % self.Name)


class Wonman(People):
    def get_birth(self):
        print("%s 生了小孩" % self.Name)


m1 = Man('Leon', 22, 5000)

m1.eat()
m1.play()
m1.sleep()

w1 = Wonman("leona", 24)

w1.eat()
w1.get_birth()
# w1.play()  # 沒有Man的功能,所以是不能使用的
