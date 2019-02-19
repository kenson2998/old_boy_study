'''
1.啟動程序後,讓用戶輸入工資,然後打印商品列表
2.允許用戶使用商品編號購買商品
3.用戶選擇商品後,檢查餘額是否足夠,夠就直接扣款,不夠就提醒
4.可隨時退出,退出時打印採購商品和餘額
'''
salarys = input('your salary：')
if salarys.isdigit():
    salarys = int(salarys)
produces = [['Iphone', 5000], ['Mar pro', 12000], ['Latte', 3100]]
shopping_cart = []
while True:
    for index, items in enumerate(produces):
        print(index + 1, items)
    buy = input('預購商品,或輸入q跳出：')
    if buy.isdigit():
        buy = int(buy)
    if (buy) == 'q':
        break
    if produces[buy - 1][1] < salarys:
        salarys -= produces[buy - 1][1]
        shopping_cart.append(produces[buy - 1][0])
        print('已購買', produces[buy - 1][0], '剩下：', salarys)
    else:
        n = input('餘額不足,請按任意鍵退出或輸入‘n’繼續選購。')
        if n == 'n':
            continue
        else:
            break
print('餘額為：＄', salarys)
for i in range(len(produces)):
    print(produces[i][0], '數量：', shopping_cart.count(produces[i][0]))
