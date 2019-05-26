import shelve

d = shelve.open('shelve_test')  # 用shelve 打開文件

# name = ['Abb', 'Baa', 'Cdd']
# info = {'age': 22, 'job': 'IT'}
#
# d['name'] = name  # 持久化列表
# d['info'] = info  # 持久化字典
# d.close()  # 會產生三個檔案 .bak , .dat , .dir , 這邊不清楚是否版本問題, 產生的是一個.db

print(d['name'],d['info'])


