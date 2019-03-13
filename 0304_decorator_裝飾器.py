'''
裝飾器：
1.定義：本質是一個函數，（裝飾其他函數）就是為其他函數添加附加功能
原則： 1.不能修改被裝飾的函數的源代碼
      2.不能修改被裝飾的函數的調用方法
實現裝飾器知識備儲：
1.函數即“變量”
2.高階函數
3.嵌套函數

高階函數 ＋ 嵌套函數 ＝ 裝飾器
'''

import time


def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return warpper


@timmer
def test1():
    time.sleep(3)
    print('in the test1')

@timmer
def test1_1(name, age):
    print(name, age)


test1()
test1_1("Leon",30)


def per(function):
    def calc(*args):
        a = function(*args)
        print((a[0]) * a[1])

    return calc


@per
def test2(a, b):
    print(a, b)
    return a, b


test2(5, 3)


# 函數嵌套

def foo():
    def func1():
        pass

    func1()
