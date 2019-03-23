import json, pickle



info = {
    "name": "Leon",
    "age": 30
}

with open('json_p.txt','w') as f:
    f.write(json.dumps(info))



def sayhi(name):
    print(name)

info = {
    "name": "Leon",
    "age": 30,
    "func": sayhi
}
# pickle 是轉為二進制
# with open('json_p.txt', 'wb') as f:
#     f.write(pickle.dumps(info))
