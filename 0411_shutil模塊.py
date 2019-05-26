# 文件複製

import shutil

f1 = open('shutil_note1', 'r')
f2 = open('shutil_note2', 'w')

shutil.copyfileobj(f1, f2)  # copy 內容

f1.close()
f2.close()
shutil.copyfile('shutil_note2', 'shutil_note3')  # copy文件
# shutil.copytree('old_dir','new_dir') #遞歸的複製目錄 #olddir和newdir都只能是目录，且newdir必须不存在
#shutil.rmtree('new_dir') # 遞歸移除目錄
# shutil.move('/sss/aaa.txt','/new_dir') # 移動文件


# 用shutil壓縮文件
shutil.make_archive('shutil_archive', 'zip', '/Users/leon/PycharmProjects/practice/老男孩python/oldboy_study/ATM')

import zipfile

# 打包 壓縮 zip
# 打包不壓縮 tar
z = zipfile.ZipFile('day5.zip', 'w')

z.write('shutil_note1')  # 指定要壓縮的檔案
print('-------')  # 中間可以做別的事情
z.write('shutil_note2')
z.close()

# 解壓
z = zipfile.ZipFile('day5.zip','r')
z.extractall()
z.close()

