
from module_leon import say_hello as say_hello_leon

def say_hello():
    print('in the main')

say_hello()
say_hello_leon()

#包本身就是一個目錄，用來邏輯上組織模塊的(必須帶有__init__.py文件)
# 導入包的本質就是執行底下的＿＿init__.py文件
import a_package