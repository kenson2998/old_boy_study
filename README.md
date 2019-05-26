## index ##

#### for ####
* 0216 for 練習
  * range(0,5,2)   #每次迴圈+2
#### list 
* 0218 list 練習
    * append  #增
    * pop  #刪除最後
    * del  #指定刪除
    * sort  #排序
    * reverse  #倒轉
    * extend  #延伸
#### copy
  * 0219_copy練習
    * deepcopy  #非位址的複製
#### dict 
* 0220_dict字典
    * get  #查
    * in  # '字串' in  dict
    * keys  # 印出字典所有key
    * values  #印出字典所有vlaue
    * setdefault('f', 'friend')  # key沒有f所以創建一個key value
    * update # 修改已有的,新增沒有的,進行合併
    * items # 將字典變成列表
    * fromkeys([1, 2, 3], ['abc', ['a', 'b', 'c'], 123])  # 給前面三個key一個對應的value“位址”
####string
* 0220_string
    * capitalize()) #首字母大寫
    * center(50,'*')) #美化打印
    * ljust(50,'-')) #補齊50個字
    * endswith('on')) #檢查結尾是否為這個字串,是為true
    * strings[strings.find('name'):]) #查找並切片
    * format_map({'name':'Leon','age':30})) #format 使用字典去格式化
    * join(['1','2','3','4']))  #添加列表內的值到字串上
    * lstrip())#左換行符號和空格符號移除
    * rstrip())#右換行符號移除
    * strip()) #左右空格和換行符號都移除
      * a = maketrans('abcdefg','1234567') #建立一組替換規則
      * translate(a) #套用規則
    * replace('a','A',2)) #可指定置換次數
    * split(' ')) #用空格來分類
####tuple 
* 0220_dict字典
    * index
    * count
