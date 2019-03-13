import time


def time_count(func):
    def times():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return times


@time_count
def funz():  # 一般寫法是產生一個實際的列表，當列表旁大時就可以看出生成時間有差距，且佔空間又浪費
    a = [i * 3 for i in range(10000000)]
    print(a)
    print(a[10])


@time_count
def func_generator():  # 生成器的方式返回的是一個公式的地址
    a = (i * 3 for i in range(10000000))
    print(a)
    # print(a[10])#無法查看，因為沒有生成


# funz()
func_generator()

c = (i * 2 for i in range(1000000000))
print(c.__next__())
print(c.__next__(),"\n")


def fib(max):  # 婓波納契數列 前兩個數相加會等於第三個值
    n, a, b = 0, 0, 1
    while n < max:  # n<10
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# f = fib(6)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
g = fib(8)
while True:
    try:
        x = next((g))
        print('g:',x)
    except StopIteration as e :
        print('Generator return value:',e.value)
        break
