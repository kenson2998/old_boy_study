import os

print('獲取當前工作目錄', os.getcwd())
print('前往目錄,相當於 cd', os.chdir('..'))
print('獲取當前目錄', os.curdir)
print('獲取當前目錄的上一層(父目錄)', os.pardir)
print('創建好幾層目錄(ex:c:\\a\\b\\c\\d),即使沒有b,c,d也能一次創建', os.makedirs(os.getcwd() + "\\a\\b\\c\\d"))
print('移除dirs,若目錄為空則刪除,如果有文件則不刪除,用於刪除空目錄的', os.removedirs(os.getcwd() + "\\a\\b\\c\\d"))
# print('創建一個目錄,若b,c不存在,則不能創造d目錄', os.mkdir('\\a\\b\\c\\d'))
# print('創建一個目錄', os.mkdir('\\a'))
# print('刪除一個目錄', os.rmdir('\\a'))
print('顯示當前目錄', os.listdir('.'))
# print('刪除一個文件', os.remove())
# print('重新命名檔案', os.rename('oldname','newname'))
print('獲取文件/目錄信息', os.stat('03'))
print('windows 顯示 \\ ,linux 顯示/  ', os.sep + 'a' + os.sep + 'b' + os.sep + 'c' + os.sep + 'd')
path_test = " \\Users\\leon\\PycharmProjects/practice/老男孩python/oldboy_study"
path_change = path_test.replace('\\', os.sep)
print('修改目錄的格式 ', path_change)

print('windows 顯示 \ t \ n ,linux 顯示 \ n  ', os.linesep)
print('windows 顯示 \ t \ n ,linux 顯示 \ n  ', os.pathsep)
print('環境變數:', os.environ)
print('顯示當前使用的os, win顯示nt , linux顯示posix :', os.name)
print(os.system('ping 8.8.8.8 -t 1'))
