import pickle, json

data1 = {'k1': 123, 'k2': 'hello'}

p_str = pickle.dumps(data1)  # 將數據以特殊型式轉換為python語言認識的字符串
print(p_str)

# with open('pickle.pk','w') as pf: #pickle 寫入文件
#     pickle.dump(data1,pf)

j_str = json.dumps(data1)  # 將數據以特殊型式轉換為所有語言認識的字符串
print(j_str)

# with open('json.json','w') as jf: #json 寫入文件
#     json.dump(data1,jf)
