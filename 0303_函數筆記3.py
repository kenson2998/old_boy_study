def func(x, y, z):  # x ,y 為形象參數,不調用時不存在
    print(x)
    print(y)
    print(z)


# x, y 為實際參數
x = 1
y = 2

# func(y=y, x=x)  # 與行參順序無關
# func(1, 2)  # 與行參一一對應
# func(1,x=2) #這樣就會報錯,因為沒有指定行參的話就會依照順序
func(1, z=2, y=3)


def func2(x, y=2):  # y是默認參數
    print('func2:', x, y)


# 默認參數特點： 調用函數時，默認參數非必須傳遞
func2(1)
func2(1, y=3)


def func3(*args):  # Ｎ個位置參數組，轉換成元祖
    print(args, type(args))


func3(1, 2, 3, 4, 5, 6)
func3(*[1, 2, 3, 4, 5])  # 等於 tuple(1,2,3,4,5)


def func4(x, *args):
    print(x)
    print(args)


func4(1, 2, 3, 4, 5, 6, 7)


def func5(**kwargs):  # Ｎ個關鍵字參數 轉換成字典格式
    print(kwargs)


func5(name='Leon', age=30, sex='m')
func5(**{"name": "leon", "age": 10})

def func6(name,age=8,**kwargs):
    print(name)
    print(age)
    print(kwargs)



func6('Leon',sex="M")
