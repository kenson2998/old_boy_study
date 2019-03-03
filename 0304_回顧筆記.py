# python2 默認用的是ascii
#python3 默認編碼是unicode
# GBK 可兼容GB2312
# unicode 存英文和中文都是兩個字節
# unicode 萬國碼
# GBK <-> Unicode <-> UTF-8  中間必須透過unicode轉換

# f = open  rb wb ab 打開的是二進制格式
# f = open('txt.txt','rb',encoding='utf-8')