'''
修改haproxy配置文件
查
1. 輸入 www.oldboy.org
2.獲取當前breakend下的所有紀錄

新建
1.輸入:arg = {
    'breakend':'www.oldboy.org',
    'record':{
        "server" : "100.1.7.9",
        "weight" : 20,
        "maxcknn": 30
    }
}


刪除
1.輸入:arg = {
    'breakend':'www.oldboy.org',
    'record':{
        "server" : "100.1.7.9",
        "weight" : 20,
        "maxcknn": 30
    }
}
'''

a = '''{
    'breakend':'www.oldboy.org',
    'record':{
        "server" : "100.1.7.9",
        "weight" : 20,
        "maxcknn": 30
    }
}'''

# print(eval(a)) # eval可將字符串變成字典
a = eval(a)

loop_gate = True

hapoxy = {}
while loop_gate:
    b = input('請選擇功能1.查詢2.新增3.刪除4.離開：')
    if b.isdigit():
        b = int(b)
        if b > 5:
            continue
        else:
            if b == 1:
                count = 0
                finds = input('輸入想查找的：')
                with open('0303_作業', 'r') as search:
                    for line in search:
                        if count == 1 :
                            if line[0] != " ":
                                count = 0
                                continue
                            print(line)

                        if finds in line :
                            print(line)
                            count = 1

            if b == 2:
                print('新增')
            if b == 3:
                print('刪除')
            if b == 4:
                print('離開')
