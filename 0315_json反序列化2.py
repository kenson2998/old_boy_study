import json,pickle

def sayhi(name):
    print('name2',name)

with open('json_p.txt','rb') as f:
    a = pickle.load(f)

    a['func']("Leon") #雖然是傳過來的func,是sayhi的地址 ,可是調用的是本地的sayhi