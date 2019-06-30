import socket

server = socket.socket()

server.bind(('localhost', 6969))

server.listen()  # 監聽

print("我要開始等電話了")
conn, addr = server.accept()  # 等待電話打進來, conn = 電話打過來的實例,addr = 客戶端口
#conn 就是客戶端連過來而在服務器端為其生成的一個實例連結
print(conn, addr)
data = conn.recv(1024)  # 接收

print("recv:", data)

conn.send(data.upper())  # 發送

server.close()
