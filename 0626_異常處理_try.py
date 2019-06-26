dea = {}
data = []
try:
    data[3]
    dea['name']
except KeyError as e:
    print('no this key', e)
except IndexError as e:
    print('列表操作錯誤:', e)

try:
    data[3]
    dea['name']
except (KeyError, IndexError) as e:
    print(e)

try:
    # data[3]
    # dea['name']
    open('eee.txt')
    pass
except (KeyError, IndexError) as e:
    print(e)
except Exception as e:
    print("出錯了", e)
else:
    print("一切正常")
finally:
    print("不管有沒有錯,都執行")

s1 = "hello"
try:
    int(s1)

except ValueError as e:
    print("錯誤類型:", e)



