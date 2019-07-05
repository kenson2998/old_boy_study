# from 0702module import aa

# 如果遇到動態import的情況,需要用字串來import的話

# import_from = input("請輸入你要improt的東西:").strip()
# import_from2 = input("請輸入你要improt的東西:").strip()

import_from = "0702module.aa"
import_from2 = 'zxc'
c = __import__(import_from, fromlist=[import_from2])

if hasattr(c, import_from2):
    func = getattr(c, import_from2)
    print(func)


# 官方建議用法
import importlib
import_from = "0702module.aa"
import_from2 = 'zxc'
b = importlib.import_module(import_from)

if hasattr(b, import_from2):
    func = getattr(b, import_from2)
    print(func)