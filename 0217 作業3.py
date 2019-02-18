# 三級菜單

relations = [['爺爺','奶奶'],['父親','母親'],['小孩','女孩','男孩']]
deep1 = 0
while True:
    print('你現在在第{deep1}層'.format(deep1=deep1))
    deep1 = int(input('你想查看哪一層（1/2)：'))
    print(relations[deep1])
