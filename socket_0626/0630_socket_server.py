import socket
import os
server = socket.socket()

server.bind(('localhost', 6666))

server.listen(5)  # 最大允許監聽數
print("我要開始等電話了")

while True:  # 第一層 while結束會監聽下一位client
    conn, addr = server.accept()  # 等待電話打進來, conn = 電話打過來的實例,addr = 客戶端口
    # conn 就是客戶端連過來而在服務器端為其生成的一個實例連結
    print(conn, addr)
    while True: # 這個client 持續接收
        data = conn.recv(1024)  # 接收
        print("recv:", data.decode())
        if not data:  # data 為空
            print("client has lost...", data)
            break

        # conn.send(data.upper())  # 發送大寫返回

        # res = os.popen(data.decode()).read() #執行linux指令
        # conn.send(res.encode("utf-8"))  # res指令結果


        f = open("video 2.mov",'rb')
        data = f.read()
        conn.send(data)

server.close()
