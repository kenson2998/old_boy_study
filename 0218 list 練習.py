
names = ['leon', 'lee', 'lion', 'leona', 'leesin']
#查
print(names[:3]) #從0開始到3的位置
print(names[-2:]) #從左邊數過來 倒數第二位到最後的位置

#增
names.append('rick')
print('添加名字到後頭',names)
names.insert(1, 'Yi master')
print('加入第1個位置', names)

#改
names[2] = 'lion fu'
print('改寫第2個位置', names)

#刪除
names.pop()
print('pop會預設刪除最後一筆', names)
del names[0]
print('del 刪除第0位', names)

names.sort()
print('排序', names)

names.reverse()
print('反轉', names)

names2 = [1,2,3,4]
#添加延伸
names.extend(names2)
print(names)