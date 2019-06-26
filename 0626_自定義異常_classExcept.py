#自定義異常
class leonException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message

try:
    raise leonException('我的異常')
except leonException as e:
    print(e)