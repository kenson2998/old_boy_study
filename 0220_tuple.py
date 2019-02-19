#元祖tuple是用來存放不可改的元素,只有count和index兩個方法可用
names = ('name', 1, 1, ['123'])
print(names.index(['123']))
print(names.count(1))
print(names, type(names))
