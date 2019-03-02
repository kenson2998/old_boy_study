oldboy = "old boy linux"

def test1(name):
    # global oldboy #設定global後就能夠改全局變數的值
    oldboy = "mage Linux"
    print("before change %s " % name , oldboy)
    name = "Leon fu" #局部變量只用在這個函數裡面
    print("After change %s" % name)
    # print(name2)

name = "leon"

test1(name)
name2 ="alex"
print(name)
print(oldboy)

#####
name3 =['abc','def','ggg']
def test2():
    name3[0] = 'aaaaaac'
print(name3)
test2()
print(name3) #全局的值在函數裡修改了，只有字串和數字是沒辦法更改的，但其他格式可以的