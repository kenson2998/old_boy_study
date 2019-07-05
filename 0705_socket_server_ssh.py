import socket, os

server = socket.socket()
server.bind(("localhost", 6698))
server.listen()
while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    data = conn.recv(1024)  # 接收大小,如果超過1024的話,會先放到緩衝區 ,下一次發送時會再收到,避免這個問題可以給大一點的值
    if not data:
        print("用戶已斷開")
        break
    print("執行指令: %s " % data)
    cmd_res = os.popen(data.decode()).read()  # data 是byte格式,所以要decode成str格式
    conn.send(str(len(cmd_res)).encode("utf-8"))  # 傳送時要encode("utf-8")成byte格式

    conn.send(cmd_res.encode("utf-8"))  # 傳送時要encode("utf-8")成byte格式

server.close()
