# 因為兩個def裡面使用了package_test.test1.test(),
# 一開始import 時只有 package_test進來,還要再做一次test1查找test()這個function
import package_test
def logger():
    package_test.test1.test()
    print('in the logger')
def search():
    package_test.test1.test()
    print('in the search')

logger()



# 有重複查找的行為，我們可以對此進行優化
# 先將package_test目錄加入sys.path,再利用from import 的方式直接將test方法導入
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/package_test')
from test1 import test
def logger1():
    test()
    print('in the logger1')
def search1():
    test()
    print('in the search1')

logger1()
