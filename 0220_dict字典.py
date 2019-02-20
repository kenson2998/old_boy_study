dicts = {
    "a": "apple",
    "b": "banana",
    "c": "cat",
    "d": "dog"
}
# 查

print(dicts.get('b'))
print('c' in dicts)
print('e' in dicts)
print(dicts.keys())
print(dicts.values())
# 改
dicts['a'] = 'account'
print(dicts)
dicts.setdefault('f', 'friend')  # key沒有f所以創建一個key value
print(dicts)
dicts.setdefault('a', 'animation')  # 因為有a的key了 所以不新增a
print(dicts)
b = {
    'a': 'anyway',
    's': 'so',
    'g': 'good'
}
dicts.update(b)  # 修改已有的,新增沒有的,進行合併
print(dicts)

print(dicts.items())  # 將字典變成列表

# 兩個方法都能找出key,vlaue ,不過速度上第一個方法比第二個方法快速,因為第二個方法必須先轉為列表
for i in dicts:
    print(i, dicts[i])

for k, v in dicts.items():
    print(k, v)
    

c = dict.fromkeys([1, 2, 3], ['abc', ['a', 'b', 'c'], 123])  # 給前面三個key一個對應的value“位址”
print(c)

c[1][2] = 456
print(c)  # 全改為456值是因為 這個fromkeys()之後改的都是同一個位址的值
