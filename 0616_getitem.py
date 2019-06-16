class Foo(object):  # 高級的地方會用到它 比如Django , 利用字典的形式去調用它
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print("__getitem__:", key)

    def __setitem__(self, key, value):
        print("__setitem__:", key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print("__delitem__:", key)


obj = Foo()
obj['name'] = "alex"
del obj['ddddd']  # 沒有ddddd也不會報錯 ,意思是使用字典去調用而已
print(obj.data)

# result = obj['k1'] #自動觸發執行 __getitem__
# obj['k2'] = "alex" #自動觸發執行 __setitem__
# del obj['k1']
