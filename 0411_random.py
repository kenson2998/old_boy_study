import random

print(random.random())  # 隨機0～1 浮點數
print(random.uniform(1, 2))  # 可自己設定浮點數區間
print(random.randint(1, 7))  # 隨機1～7 整數, 包含7
print(random.randrange(7))  # range 顧頭不顧尾, 0~7的範圍, 不包含7
print(random.randrange(1,101))
print(random.choice('hello'))  # 隨機選擇可傳入可遞歸的東西,'字串',[1,2,3],["hello"]
print(random.sample('hello', 2))  # 可在後面設定要取幾位
list_a = [x for x in range(1,5)]
random.shuffle(list_a)  # 洗牌功能
print(list_a)