'''
函數優點
1.代碼重用
2.保持一致性
3.可擴展性


'''

def logger():
    with open('function_practice.txt','a+') as f :
        f.write('log write \n')

def func1():
    '''test1'''
    print('func1')
    logger()
def func2():
    '''test2'''
    print('func2')
    logger()
def func3():
    '''test3'''
    print('func3')
    logger()

func2()
func1()
func3()
