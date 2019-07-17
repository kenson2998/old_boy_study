import socket

client = socket.socket()
client.connect(("localhost", 6698))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 1: break
    client.send(cmd.encode("utf-8"))
    data = client.recv(1024)
    print("命令結果大小", data)
    rec_size = 1024
    rec_size += int(data.decode())
    while rec_size > int(data.decode()):
        data1 = client.recv(rec_size)
        print("秀一波:\n", data1.decode())
        break
    else:
        print('recv size....', rec_size)

client.close()

# 上到第八週第11
