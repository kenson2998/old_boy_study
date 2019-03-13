import time


def consumer(name):
    print("%s 準備吃包子拉" % name)
    while True:
        baozi = yield
        print("包子[%s]來了，被[%s]吃了！" % (baozi, name))

# c = consumer('Leon')
# c.__next__()#next只是調用yield
#
# b1 = "豆沙"
# c.send(b1) #send可以給yield傳值


def producer(name):
    #先生成兩個消費者
    c = consumer('A')
    c2 = consumer('B')
    #然後初始化
    c.__next__()
    c2.__next__()
    print("%s準備開始做包子拉" %name)
    for i in range(10):
        time.sleep(1)
        print("做了兩個包子,一個豆沙，一個鮮肉")
        c.send(i)
        c2.send(i)

producer('Leon')