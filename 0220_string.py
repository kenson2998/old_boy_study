strings = 'my name is Leon'

print(strings.capitalize()) #首字母大寫
print(strings.center(50,'*')) #美化打印
print(strings.ljust(50,'-')) #補齊50個字
print(strings.endswith('on')) #檢查結尾是否為這個字串,是為true
print(strings[strings.find('name'):]) #查找並切片
str1 = 'my name is {name} , {age} years old'
print(str1.format_map({'name':'Leon','age':30})) #format 使用字典去格式化
print('+'.join(['1','2','3','4']))  #添加列表內的值到字串上
print('\n  Leon'.lstrip())#左換行符號和空格符號移除
print('Leon\n')
print('Leon\n'.rstrip())#右換行符號移除
print('  Leonzasdd\n'.strip()) #左右空格和換行符號都移除

p = str.maketrans('abcdefg','1234567') #建立一組替換規則
rep = str.maketrans('1234567', 'abcdefg')
print('leon fu'.translate(p)) #套用規則
recode = 'leon fu'.translate(p)
print(recode.translate(rep))

print('abcdefsaaa'.replace('a','A',2)) #可指定置換次數
print('Leon fu'.split(' ')) #用空格來分類