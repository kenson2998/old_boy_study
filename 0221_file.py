# 讀取
f = open('file_p', 'r')
data = f.read()
print(data)
f.close()

# append 追加寫入
f = open('file_p', 'a+')
# f.write('i like\n')

f.close()

# 讀取前五行資料
f = open('file_p', 'r')
for i in range(4):
    print(f.readline().strip())
f.close()

# 第四行不印
# low loop
# f = open('file_p', 'r')
# for index, line in enumerate(f.readlines()):
#     if index == 3:
#         print('不列印')
#         continue
#     print(line.strip())
# f.close()

# high bige
f = open('file_p', 'r')
count = 0
for line in f:
    if count == 3:
        count += 1
        print('不列印')
        continue
    print(line.strip())
    count += 1
f.close()
