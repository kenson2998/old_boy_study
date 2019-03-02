# def calc(n):
#     print(n)
#     return calc(n + 1)
#
#
# calc(0) # 沒有給停止條件會無限循環，所以最大做到999次有一個停止機制報錯

#遞歸的特性：
# 1.必須要有明確的停止條件
# 2. 每進入一層遞歸，規模要比上一層更少
# 3.遞歸效率不高


def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))
    print('->',n)

calc(10)