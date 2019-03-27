import time

# 時間戳是從1970開始算起,透過運算可以解釋為現在的時間,例如下方算出現在年份
x = time.time()
x = x/3600/24/365
x2 = int(x)+1970
print('1970 + %s = ' % int(x), x2)

# 公元時間
print(time.gmtime())
# 本地時間
print(time.localtime())

print(time.localtime().tm_year)