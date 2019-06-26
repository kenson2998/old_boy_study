# 自定義異常
class leonException(Exception):
    def __init__(self, msg):
        self.message = msg
        self.sss = msg + "234"

    def __str__(self):  # __str__ 用於定義返回的值為什麼格式
        return self.message
        # return '我是異常例外喔'


try:
    raise leonException('我的異常')  # raise (瑞斯) 觸發的意思
except leonException as e:
    print(e)
