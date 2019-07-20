import os

print(os.getcwd())  # 獲取執行檔的當前目錄

os.chdir('/Users/leon/PycharmProjects/practice/老男孩python/')  # 前往目錄
print(os.getcwd())
print(os.listdir(os.getcwd()))  # 查詢一個目錄下的所有目錄與檔案,包含隱藏檔案
print(os.sep)  # 相當於windows下的\\,linux下的/
print(os.path.split('/user/a/c/a.txt'))  #切割目錄和檔名
print(os.path.exists('/Users/leon/PycharmProjects/practice/老男孩python/'))
print(os.path.join('/usr', '/abc')) # 目錄合併