
import json,pickle
def sayhi(name):
    print(name)

info = {
    "name": "Leon",
    "age": 30,
    "func": sayhi
}
with open('json_p.txt','wb') as f :

    pickle.dump(info,f)
    pickle.dump(info,f)