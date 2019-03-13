'''
迭代器
可以直接作用於for循環的數據類型有：
一類是集合數據類型：list、tuple、dict、set、str
一類是generator,包含生成器和帶yield的generator function
這些可以作用於for循環的對象稱為迭代對象：Iterable
可以使用isinstance()判斷是否是Iterable對象。
'''
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

'''
list、dict、str是Iterable但不是Iterator,
不過可以透過iter()函數來獲得一個Iterator對象
'''
a = iter([])
print(a, isinstance(a, Iterable))


'''
生成器可以被next調用並不斷返回下一個值的對象稱為迭代器：Iterator
可以使用isinstance()判斷是否是Iterator對象。
'''
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))

