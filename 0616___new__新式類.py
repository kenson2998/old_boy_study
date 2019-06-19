def func(self):  # 定義一個function, 之後要包裝成class 所以先給他self
    print("hello %s " % self.name )

def initt(self,name,age):
    self.name = name
    self.age = age

'''創建class, 一個Foo對象 
(object,) <~必須加逗點,因為他是元祖的形式,你不加一個逗點他就把它當作一個值了,加了逗點他才知道你是元祖的形式
'''
Foo = type("Foo", (object,), {"talk": func, "__init__": initt})

print(type(Foo))

f = Foo('Leon',24)  # 一樣可以創建class對象

f.talk()  # f對象裡面有talk這個def可以使用
