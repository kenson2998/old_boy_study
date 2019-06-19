class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("---MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call--")
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print("Foo --init--")

    def __new__(cls, *args, **kwargs): #會比init還早做完, 如果沒有return就不會接著做init(實例化)
        print("Foo --new--")
        return object.__new__(cls) 


# 第一階段： 解釋器從上到下執行代碼創建Foo類
# 第二階段： 通過Foo類創建obj對象
obj = Foo("Alex")
# obj1 = MyType("Alex")
