def bulk(self):
    print("%s is talking" % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating" % self.name, food)


d = Dog('Leon')

choice = input(">>:").strip()  # 輸入eat
'''
d.choice()  #沒辦法使用輸入的東西去調用eat,因為choice是一個字符串,
除非你用 if 去判斷

if choice == "eat":
    d.eat()
    
    
但不能用 
if choice in d :  #因為他不是一個字典   
'''

# 反射工具
print("查找對象是否有這個方法:", hasattr(d, choice))  # 回傳True or False
# print("查找對象是否有這個方法,並打印他的位址:", getattr(d, choice))
# getattr(d, choice)()

# 反射用法
# hasattr setattr
'''
if hasattr(d, choice):
    func = getattr(d, choice)
    func('cake')

else:
    print('%s has no %s function' % (d.name, choice))
    # 沒有這個方法的時候,我想要加上一個方法
    if choice == 'talk':
        setattr(d, choice, bulk) # 相當於 d.talk = bulk 
        s = getattr(d, choice)
        print('已加入這個方法：%s,  d.talk:%s' % (s, d.talk))
        getattr(d, choice)(d)

        d.talk(d)

'''

# setattr
'''
if hasattr(d, choice):
    setattr(d, choice, 'Leona') # attr 有name的話 , 輸入name時,我們會獲得leon,所以我們測試改name的值
    print(getattr(d, choice))
print(d.name)
'''

# delattr  輸入name 來測試刪除name
if hasattr(d, choice):
    delattr(d, choice)

    print('剛剛del了name:', hasattr(d, choice))
    print(d.name)  # 此時會報錯
