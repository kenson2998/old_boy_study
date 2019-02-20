list_1 = [1, 3, 5, 7, 2, 4, 6, 8]
list_1 = set(list_1)
print(list_1, type(list_1)) #進行排序, 雖然用大括號包起來,但是它不是字典格式

list_2 = set([0,66,5,4,6,22])
print(list_2)

#交集
print('交集', list_1.intersection(list_2))
print('交集', list_1 & list_2)
#聯集 去重複
print('聯集', list_1.union(list_2))
print('聯集', list_1 | list_2)

#差集 我有你沒有

print('差集', list_1.difference(list_2))
print('差集', list_2.difference(list_1))
print('差集', list_1 - list_2, list_2 - list_1)

#子集
list_3 = set([1, 2, 6])
print(list_3.issubset(list_1))
#父集
print(list_1.issuperset(list_3))

#對稱差集
print(list_1.symmetric_difference(list_2))
print('對稱差集', list_1 ^ list_2 )

list_4 = set([3, 4, 7])
print(list_3.isdisjoint(list_4)) #沒有任何交集就回傳true

# 添加
list_1.add(999)
print(list_1)
# 多值添加
list_1.update([777,8888,99999])
print(list_1)

#刪除
list_1.pop() #隨機刪除
list_1.remove(777)#如果裡面沒有這個東西會報錯,有就刪除
list_1.discard('333')# 如果有這個就刪除，沒有也不會報錯
print(list_1)