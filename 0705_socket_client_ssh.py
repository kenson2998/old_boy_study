import socket

client = socket.socket()
client.connect(("localhost", 6698))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: break
    client.send(cmd.encode("utf-8"))
    print(cmd)
    data = client.recv(10240000)  # 接收的bytes 大小,如果設定太小有可能會無法接收過大的檔案
    print("recv:", data.decode())

client.close()
