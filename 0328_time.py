import time

# 時間戳是從1970開始算起,透過運算可以解釋為現在的時間,例如下方算出現在年份
x = time.time()
print('time.time():', x)
x = x / 3600 / 24 / 365
x2 = int(x) + 1970
print('1970 + %s = ' % int(x), x2)
print('\n')
# 將struct_time格式轉為時間戳
print('time.mktime(time.gmtime()):',time.mktime(time.gmtime()))
print('\n')
# 公元時間
print(time.gmtime())
# 本地時間
print(time.localtime())
# 獲取年
print(time.localtime().tm_year)
print('\n')
# time.strftime("格式", 時間) struct_time格式轉換成你想要的時間格式
# time.strptime(時間, "格式") 依照提供的時間,對應轉換的格式,轉回struct_time的格式
y = time.localtime()
z = time.strftime('%Y - %m/%d %H:%M:%S', y)
print('z:', z)
print('z轉回struct格式：', time.strptime(z, '%Y - %m/%d %H:%M:%S'))


# 使用這個格式顯示時間：Fri Mar 29 06:00:09 2019 (%a %b %d %H:%M:%S %Y)
print(time.asctime()) # 接受元組tuple格式
print(time.ctime())   # 接受時間戳格式