# -*- coding:utf-8 -*-
import sys

print(sys.getdefaultencoding())

# unicode 中英文都是兩個位元組
# utf-8 中文是3位元 英數是1位元組

# utf-8 是 unicode 的擴展 ,所以unicode編碼可以顯示中文字

# ascii 一開始用來顯示英文的,不過最多只有256個符號，已使用了128個符號

a = '哈哈'
b = a.encode('gbk')
print(b.decode('gbk').encode('utf-8'))
