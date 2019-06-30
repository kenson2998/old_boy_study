import socket

client = socket.socket()

client.connect(('localhost', 6969))

client.send(b"hello world") #python3 只能發byte類型的字節,python2 才可以發字符串

data = client.recv(1024)

print("recv:", data)

client.close()
