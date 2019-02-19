'''
1.啟動程序後,讓用戶輸入工資,然後打印商品列表
2.允許用戶使用商品編號購買商品
3.用戶選擇商品後,檢查餘額是否足夠,夠就直接扣款,不夠就提醒
4.可隨時退出,退出時打印採購商品和餘額
'''
salarys = int(input('your salary：'))
produces = ['1.Iphone', '2.Mar pro', '3.Latte']
prices = [5000, 12000, 3100]
shopping_cart = []
while True:

    print(produces)
    buy = (input('預購商品,或輸入n跳出：'))
    if str(buy) == 'n':
        break
    else:
        buy =int(buy)
    if prices[buy - 1] < salarys :
        salarys -= prices[buy - 1]
        shopping_cart.append(produces[buy - 1])
        print('已購買', produces[buy - 1], '剩下：', salarys)
    else:
        n = input('餘額不足,請按任意鍵退出或輸入‘n’繼續選購。')
        if n == 'n':
            continue
        else:
            break
print('餘額為：＄', salarys)
for i in range(len(produces)):
    print(produces[i], '數量：', shopping_cart.count(produces[i]))
