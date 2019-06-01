## python note list ##
    
#### python
* [0304_回顧筆記](https://github.com/kenson2998/old_boy_study/blob/master/0304_回顧筆記.py)
python2 默認用的是ascii
python3 默認編碼是unicode
GBK 可兼容GB2312
unicode 存英文和中文都是兩個字節
unicode 萬國碼
GBK <-> Unicode <-> UTF-8  中間必須透過unicode轉換
f = open  rb wb ab 打開的是二進制格式
f = open('txt.txt','rb',encoding='utf-8')


#### for 
* [0216 for 練習](https://github.com/kenson2998/old_boy_study/blob/master/0216%20for%E7%B7%B4%E7%BF%92.py)
  * range(0,5,2)   #每次迴圈+2
#### list 
* [0218 list 練習](https://github.com/kenson2998/old_boy_study/blob/master/0218%20list%20%E7%B7%B4%E7%BF%92.py)


| 函數      | 註解      |
| -------- | -------- |
| append|增     |
| pop     | 刪除最後     |
| del     | 指定刪除     |
| sort     | 排序     |
| reverse     | 倒轉     |
| extend     | 延伸     |

#### copy
  * [0219_copy練習](https://github.com/kenson2998/old_boy_study/blob/master/0219_copy%E7%B7%B4%E7%BF%92.py)

| 函數      | 註解      |
| -------- | -------- |
| deepcopy     | 非位址的複製     |

#### dict 
* [0220_dict字典](https://github.com/kenson2998/old_boy_study/blob/master/0220_dict%E5%AD%97%E5%85%B8.py)


| 函數      | 註解      |
| -------- | -------- |
| get     | 查     |
| in     |  "字串" in  dict , 回應 True or False    |
| keys     | 印出字典所有key     |
| values     | 印出字典所有vlaue     |
| setdefault('f', 'friend')     | key沒有f所以創建一個key value     |
| update     | 修改已有的,新增沒有的,進行合併     |
| items     | 將字典變成列表     |
| fromkeys([1, 2, 3], ['abc', ['a', 'b', 'c'], 123])     | 給前面三個key一個對應的value“位址”     |


#### string
* [0220_string](https://github.com/kenson2998/old_boy_study/blob/master/0220_string.py)

    
| 函數      | 註解      |
| -------- | -------- |
| capitalize()   | 首字母大寫    |
| center(50,'*')     | 美化打印     |
| ljust(50,'-')     | 補齊50個字     |
| endswith('on')     | 檢查結尾是否為這個字串,回傳True or False     |
| strings[strings.find('name'):]     | 查找並切片     |
| format_map({'name':'Leon','age':30})     | format 使用字典去正規化     |
| join(['1','2','3','4']))      | 添加列表內的值到字串上    |
| lstrip()    | 左換行符號和空格符號移除     |
| rstrip()    | 右換行符號移除     |
| strip()    | 左右空格和換行符號都移除     |
| replace('a','A',2)   | 可指定置換次數     |
| split(' ')   | 用空格來分類     |
      a = maketrans('abcdefg','1234567')    #建立一組替換規則 
      translate(a)   #套用規則 


#### tuple 
* [0220_tuple](https://github.com/kenson2998/old_boy_study/blob/master/0220_tuple.py)

| 函數      | 註解      |
| -------- | -------- |
| index     | 索引查詢     |
| count     | 計算出現次數     |
#### file
* [0221_file](https://github.com/kenson2998/old_boy_study/blob/master/0221_file.py)
* [0301_文件修改](https://github.com/kenson2998/old_boy_study/blob/master/0301_%E6%96%87%E4%BB%B6%E4%BF%AE%E6%94%B9.py)

| 函數      | 註解      |
| -------- | -------- |
| open(file,'r')     | 讀檔案     |
| open(file,'w')     | 寫檔案     |
| open(file,'a')     | 加寫檔案     |

      f = open(file,'r') 
      f.readline() #讀取行
      f.tell() #顯示光標位置
      f.seek() #讓光標回到0
      f.close() #關閉檔案


| 另一開檔方法      | 註解      |
| -------- | -------- |
|with open(file,'r') as f: |這種寫法不需要下f.close()|

    雙開檔案 一讀一寫
    
    with open('file_p', 'r') as f, \
     open('file_p_修改', 'w') as f_new:

     
#### set
* [0221_set集合](https://github.com/kenson2998/old_boy_study/blob/master/0221_set集合.py)
#
    set1 = set([1,2,3,4,5]) #一個集合
        
| 函數      | 另一種相同寫法      | 註解      |
| -------- | -------- |-------- |
| set1.intersection(set_2)     | set1 `&` set2     | 交集         |
| set1.union(set_2)     | list_1 `|` list_2    | 聯集 去重複       |
| set1.difference(set2)   | set1 `-` set2     | 差集 我有你沒有     |
| set3.issubset(set1)     |    | 子集     |
| set1.issuperset(set3)   |    | 父集     |
| set1.symmetric_difference(set2)   | set1 `^` set2   | 對稱差集   |
| set1.isdisjoint(set4)   |    | 沒有任何交集就回傳true     |
| set1.add(999)   |    | 添加     |
| set1.update([777,8888,99999])   |    | 多值添加     |
| set1.pop()   |    | 隨機刪除     |
| set1.remove(777)   |    | 如果裡面沒有這個東西會報錯,有就刪除     |
| set1.discard('333')   |    | 如果有這個就刪除，沒有也不會報錯     |
#### sys
* [0301_文件修改](https://github.com/kenson2998/old_boy_study/blob/master/0301_文件修改.py)
* [0302_unicode](https://github.com/kenson2998/old_boy_study/blob/master/0302_unicode.py)

| 函數      | 註解      |
| -------- |-------- |
|argv|接受cmd的訊息
|getdefaultencoding()|獲取當前預設的解碼
|decode('gbk')|編碼"簡體"
|encode('utf-8')|解碼"utf-8"

    >>>python script.py 1 2 3 4
    print(argv)
    >>>['script.py','1','2','3','4']
    argv[1]
    >>>1
    
#### def 
* [0302_函數筆記1](https://github.com/kenson2998/old_boy_study/blob/master/0302_函數筆記1.py)
* [0302_函數筆記2](https://github.com/kenson2998/old_boy_study/blob/master/0302_函數筆記2.py)
* [0302_函數筆記3](https://github.com/kenson2998/old_boy_study/blob/master/0302_函數筆記3.py)
* [0303_局部變量](https://github.com/kenson2998/old_boy_study/blob/master/0303_局部變量.py)
* [0303_遞歸(迴)筆記](https://github.com/kenson2998/old_boy_study/blob/master/0303_遞歸筆記.py)
* [0303_高階函數](https://github.com/kenson2998/old_boy_study/blob/master/0303_高階函數.py)
* [0304_decorator_裝飾器、嵌套函數](https://github.com/kenson2998/old_boy_study/blob/master/0304_decorator_裝飾器.py)(定義在這看)
* [0312_局部作用域和全域訪問順序](https://github.com/kenson2998/old_boy_study/blob/master/0312_局部作用域和全域訪問順序.py)
* [0313_decorator進階](https://github.com/kenson2998/old_boy_study/blob/master/0313_decorator進階.py)


```python
#宣告函數
def foo():
    print('123')
```
```python
#裝飾器
def decorator(func):
    def warpper(*args, **kwargs):
        ccc = 0
        func(*args, **kwargs)
        ddd = 0
    return warpper
    
@decorator
def func1():
    aaa = 0
    bbb = 0

func1()
```


```
otherdeco = decorator(func1) ＃另一種裝飾的用法
```
| 裝飾後的func()執行順序      |  內容     |
| -------- |-------- |
|1|func()
|2|ccc = 0
|3|aaa = 0
|4|bbb = 0
|5|ddd = 0

```python
#嵌套函數
def foo():
    def func1():
        pass

    func1()
```

```python
#decorator進階
def auth(auth_type):
    print("auth func:",auth_type)

    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            pass
        return wrapper
    return out_wrapper

@auth(auth_type = "local")
def form_page():
    pass
```
    
    
    
#### Iterable
* [0314_Iterator＿迭代器](https://github.com/kenson2998/old_boy_study/blob/master/0314_Iterator＿迭代器.py)(定義在這看)

| 函數      | 註解      |
| -------- |-------- |
|Iterable|判斷是否能夠迭代,回傳True or False
|Iterator|判斷是否是Iterator對象,回傳True or False

```python
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

'''
生成器可以被next調用並不斷返回下一個值的對象稱為迭代器：Iterator
可以使用isinstance()判斷是否是Iterator對象。
'''
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))

```




#### generator
* [0314_generator列表生成](https://github.com/kenson2998/old_boy_study/blob/master/0314_generator列表生成.py)(發現筆記他媽完整 就不整理了)

| 函數      | 註解      |
| -------- |-------- |
|.__next__()|查詢,查詢之前不會產生所以用next查詢時才會產生
||

比一般產生的速度和佔容量大小更優秀
```python
# 生成器的方式返回的是一個公式的地址
a = (i * 3 for i in range(10000000))
# 一般定義的列表
a = [i * 3 for i in range(10000000)]
```


#### demo
* [03](https://github.com/kenson2998/old_boy_study/blob/master/0304_decorator_裝飾器.py)

| 函數      | 註解      |
| -------- |-------- |
||
