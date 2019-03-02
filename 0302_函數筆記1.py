'''
面向對象：類 -> class
面向過程：過程 -> def
函數式編程：函數 -> def
'''

#函數
def func1(): # def:定義函數的關鍵字 func1:函數名
    '''testing1''' #文檔描述
    print("using this func1") #泛指代碼區塊和邏輯處理
    return 0 #定義返回值
#過程
def func2():
    '''testing2'''
    print("using this func2")


x = func1()
y = func2()

print('func1 return %s' %x)
print('func2 return %s' %y)
