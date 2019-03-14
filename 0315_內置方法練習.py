# 過濾
res = filter(lambda x: x > 3, range(10))
for i in res:
    print(i)

print('\n')

# 個別運算
res = map(lambda x: x * 2, range(10))
for i in res:
    print(i)

# 產生列表
res = [x * 2 for x in range(10)]
print(res)

# 累加
import functools

res = functools.reduce(lambda x, y: x + y, range(3))
print(res)

# 相除取商和餘數
print(divmod(10, 3))

# 排序
a = {1: 2, 4: 32, 44: 12, -2: 46}
print(sorted(a.items()))  # 依照key排序
print(sorted(a.items(), key=lambda x: x[1]))  # 依照value排序

# 兩個元素對應,拼接
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = {}
for i, k in zip(a, b):
    print(i, k)
    c[i] = k
print(c)


#map 在一個可以迭代的（iterable）的元素，遍歷使用函數
def square(x):
    return x ** 2  # 算出平方


a = map(square, [1, 2, 3, 4, 5])
for i in a:
    print(i)
