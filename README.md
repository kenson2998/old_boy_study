## python note list ##

#### for ####
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


| 函數      | 註解      |
| -------- | -------- |
| open(file,'r')     | 讀檔案     |
| open(file,'w')     | 寫檔案     |
| open(file,'a')     | 加寫檔案     |
      f = open(file,'r') 
      f.readline() #讀取行
      f.tell() #顯示光標位置
      f.seek() #讓光標回到0
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
