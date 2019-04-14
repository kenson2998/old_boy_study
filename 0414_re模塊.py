import re

# 正折表達式
print(re.match('^chen', 'chenronghua'))
res = re.match('^chen', 'chenronghua')
#  <_sre.SRE_Match object; span=(0, 4), match='chen'>
if res != None:  # 有匹配到就打印裡面的值, 沒匹配到會顯示None
    print(res.group())  # 打印值

# 匹配文字並且也找出後方的數字
res1 = re.match('^chen\d', 'chen321ronghua123')  # \d單一個數字
print(res1.group())
res1 = re.match('^chen\d+', 'chen321ronghua123')  # ＋號代表多個
print(res1.group())

res1 = re.match('.', 'chen321ronghua123')  # . 匹配任一字元,除了\n
print(res1.group())

res2 = re.search('r.+', 'chen321ronghua123')  # match 是從頭開始匹配, search可以從中搜索
print(res2.group())
res2 = re.search('r.+a', 'chen321ronghua123')  # 想找到結尾是a
print(res2.group())
res2 = re.search('r[a-z]+a', 'chen321ronghua123aaaa')  # 想找到結尾是a
print(res2.group())

res2 = re.search('[a-z]+', '123#hello#')  # 找中間hello
print(res2.group())
res2 = re.search('#.+', '123#hello#')  # 找中間#hello#
print(res2.group())

res3 = re.search('abc{2}', 'alexabcccaaa')  # 找abc,c是兩個
print(res3)
res3 = re.search('(abc){2}', 'alexabcabc')  # 把abc包起來,就變成找兩次
print(res3)

res3 = re.search('(abc){2}\|', 'alexabcabc|')  # 碰到｜符號時,要用\來表示是需要找的字,而非符號
print(res3)

res4 = re.search('(?P<id>[0-9]+)', 'abcd1234bcd@23').groupdict()  # 可直接轉成dict
print(res4)
res4 = re.search('(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)', 'abcd1234bcd@23').groupdict()  # 可直接轉成dict
print(res4)

res5 = re.search('(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})', '371481199306143242').groupdict(
    'city')  # 身分證切割運用
print(res5)

# 切割
res6 = re.split('[0-9]', 'ab134de234vbf563dw')  # 依數字分割,但是會出現空字串‘’
print(res6)
res6 = re.split('[0-9]+', 'ab134de234vbf563dw')  # 依數字分割,用個+號就可以移除空字串
print(res6)

# 替換
res7 = re.sub('[0-9]', '|','ab134de234vbf563dw')  # 找到數字為格式的就替換成|
print(res7)
res7 = re.sub('[0-9]', '|','ab134de234vbf563dw',count=2)  # 找到數字為格式的就替換成|,只換兩次
print(res7)