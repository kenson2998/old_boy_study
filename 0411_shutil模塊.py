# 文件複製

import shutil

f1 = open('shutil_note1', 'r')
f2 = open('shutil_note2', 'w')

shutil.copyfileobj(f1, f2)  # copy 內容

f1.close()
f2.close()
shutil.copyfile('shutil_note2', 'shutil_note3')  # copy文件

# 用shutil壓縮文件
shutil.make_archive('shutil_archive', 'zip', '/Users/leon/PycharmProjects/practice/老男孩python/oldboy_study/ATM')

import zipfile

# 壓縮
z = zipfile.ZipFile('day5.zip', 'w')

z.write('shutil_note1')  # 指定要壓縮的檔案
print('-------')  # 中間可以做別的事情
z.write('shutil_note2')
z.close()

# 解壓
z = zipfile.ZipFile('day5.zip','r')
z.extractall()
z.close()
