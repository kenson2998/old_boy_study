import socket

client = socket.socket()  # 聲明socket 類型,同時生成socket連接對象

client.connect(('localhost', 6666))

while True:
    msg = input("想發什麼:").strip()
    # client.send(b"Hello world") #python3 只能發byte類型的字節,python2 才可以發字符串
    # client.send("我要下載a片".encode("utf-8")) #python3 只能發byte類型的字節,python2 才可以發字符串
    if len(msg) == 0: continue  # 如果輸入為空值,會直接卡死,所以用continue到下一次回圈
    client.send(msg.encode("utf-8"))

    data = client.recv(10240000)  # 接收的bytes 大小,如果設定太小有可能會無法接收過大的檔案
    print("recv:", data.decode())

    f = open('video 2.mov', 'wb')
    f.write(data)
    f.close()

client.close()
