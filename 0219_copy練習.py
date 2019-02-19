import copy
names = ['1','2','3',[3.5,3.8],'4','5','6']
# name2 = names.copy()
name2 = copy.deepcopy(names)
# name2 =names

print(names)
print(name2)

names[3][0]=7
print(names)
print(name2)