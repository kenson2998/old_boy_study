x = 0

def grandfa():
    x = 1
    def father():
        x = 2
        def son():
            x = 3
            print(x)

        son()
    father()
grandfa()

import time
def deco(func):
    start_time = time.time()
    func()
    end_time = time.time() - start_time

    print('this time is %s'  % end_time)
    return func

def test1():
    time.sleep(3)
    print("in the test1")


def test2():
    time.sleep(3)
    print("in the test2")

test3 = deco(test1)

print(test3)

