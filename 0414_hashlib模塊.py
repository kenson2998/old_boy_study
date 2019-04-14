import hashlib

m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest()) #hex格式加密
m.update(b'Its me')
print(m.hexdigest())
m.update(b'Its too long to buy something')
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'HelloIts me') #中間沒空格 但md5加密後的值卻相同
print(m2.hexdigest())

s2 = hashlib.sha1()
s2.update(b'HelloIts me')
print(s2.hexdigest())


import hmac #用於訊息加密

h = hmac.new(b'sky king against tiger', b'you are 250')

print(h.digest())
print(h.hexdigest())