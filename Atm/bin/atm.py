

print(__file__) #找到的是相對路徑

import os
print(os.path.abspath(__file__)) #可以找到絕對路徑

print(os.path.dirname(os.path.abspath(__file__))) #可以只保留父親名

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #再加一層可以到上一層目錄

import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

import conf,core #這樣就可以import 其他目錄了
from conf import settings
from core import main

main.login()
