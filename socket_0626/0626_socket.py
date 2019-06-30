'''
OSI 七層:
應用層
展示層
會話
傳輸
網路 ip
數據鏈結  mac 地址
物理層


這些協定大多在傳輸層
http 網站協議
smtp Email
dns 網址轉譯
ftp 上下載文件
ssh 終端
snmp 簡單網路監控
icmp ping包 #此為網路層 ip
dhcp IP地址
....

網路傳輸的本質為:
A -> B
A <- B
發 send
收 receive


網路層到傳輸層之前需要遵從通信規則:
TCP/IP 協議
進行三次握手,四次斷開
UDP 協議 (直撥串流):
負責不安全的數據發送


socket 就是在做 將 協定和傳輸功能(send&receive) 的封裝,依照需求做定義來收發數據


***Socket Families 地址簇***
socket.AF_UNIX unix 本機進程間通信
socket.AF_INET IPV4
socket.AF_INET6 IPV6




*** Socket Types***
socket.SOCK_STREAM # for tcp
socket.SOCK_DGRAM # for udp
socket.RAW  #原始套接字 可用於偽造IP
socket.RDM # 可靠的UDP形式

'''
