# 修改內容並寫入新的文件
# f = open('file_p', 'r', encoding='utf-8')
# f_new = open('file_p_修改', 'w', encoding='utf-8')
import sys

#
find_str = sys.argv[1]
replace_str = sys.argv[2]
print(find_str, replace_str)


# for i in f.readlines():
#     if find_str in i:
#         i = i.replace(find_str, replace_str)
#         f_new.write(i)
#
# f.close()
# f_new.close()
#
#或是使用with 開啟兩個檔案,就不用另外寫close
with open('file_p', 'r') as f, \
     open('file_p_修改', 'w') as f_new:
    print(f.readline())
    for i in f.readlines():
        if find_str in i:
            i = i.replace(find_str, replace_str)
            f_new.write(i)
