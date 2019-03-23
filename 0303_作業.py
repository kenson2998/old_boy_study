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
    'backend':'www.oldboy.org',
    'record':{
        "server" : "100.1.7.9",
        "weight" : 20,
        "maxcknn": 30
    }
}'''
'''
backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 30
'''
# print(eval(a)) # eval可將字符串變成字典
a = eval(a)


loop_gate = True

hapoxy = {}
while loop_gate:
    b = input('請選擇功能1.查詢2.新增3.刪除4.離開：')
    if b.isdigit():
        b = int(b)
        if b < 5:
            if b == 1:
                count = False
                finds = input('輸入想查找的：')
                with open('0303_作業', 'r') as search:
                    for line in search:
                        if count:
                            if line[0] != " ":
                                count = False
                                continue
                            print(line)

                        if finds in line:
                            print(line)
                            count = True

            if b == 2:
                with open('0303_作業', 'a+') as f:
                    cont1 = '        '
                    for k, v in a.items():
                        if isinstance(v, dict):
                            for kk, vv in v.items():
                                cont1 += str(kk) + ' ' + str(vv) + ' '
                            f.write(cont1 + '\n')
                        else:
                            f.write(k + ' ' + v+'\n')

            if b == 3:
                print('刪除')
            if b == 4:
                break

'''
global
        log 127.0.0.1 local2
        daemon
        maxconn 256
        log 127.0.0.1 local2 info
defaults
        log global
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        option  dontlognull

listen stats:8888
        stats enable
        stats uri       /admin
        stats auth      admin:1234

frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.oldboy.org
        use_backend www.oldboy.org if www

backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 30
'''
