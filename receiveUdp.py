import socket


# 接收udp报文
def recUdp():
    # udp_socket = socket.socket(参数1，参数2)
    # 参数1： AF_INET表示服务器和服务器之间的通信，基于IPv4，AFA_INET6表示基于IPV6方式的服务器与服务器之间的通信
    # 参数2： socket.SOCK_DGRAM表示基于UDP报文式数据通信，socket.SOCK_STREAM表示基于TCP的流式socket通信
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字，ipv4，UDP类型
    local_addr = ("", 62436)  # 设置本地的端口，一般不写ip地址
    udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配

    t = 10  # 循环10次
    while (t > 0):
        recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改

        # 4. 显示对方发送的数据
        # 接收到的数据recv_data是一个元组
        # 第1个元素是对方发送的数据
        # 第2个元素是对方的ip和端口
        # print(recv_data)#输出接收到的原始数据数据是一个元组(b'\x8e\x10\x02\x00\x90\xbe\x0c\x01Q\x00\x00\x89`\xc2\x00\x00?\x000\x11(}\x8d', ('127.0.0.1', 10360))
        # 注意如果发送和解码方式不一样会报错！（）type类型都是bytes，但是一个是asc一个是hex解码方式不同）
        # 1.如果是Hex发送，  解码得到8e10020090be0c015100008960c200003f003011287d8d
        result_recv_data = recv_data[0].hex()  # 接收的数据类型为Hex
        # 2.如果是ASCII发送，解码得到8E 10 02 00 90 BE 0C 01 51 00 00 89 60 C2 00 00 3F 00 30 11 28 7D 8D

        # result_recv_data = recv_data[0].decode('utf-8')  # 接收的数据类型为ASCII

        print(result_recv_data)  # 打印数据
        t = t - 1
    # 3.关闭套接字
    udp_socket.close()


# 发送udp报文
def sendUdp():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sendtext = "hello"  # 表示发送的内容
    # udp_socket.sendto("发送的内容".encode("编码格式"), ("目的ip", "目的端口号"))
    udp_socket.sendto(sendtext.encode("utf-8"), ("127.0.0.1", 10360))

    # 3.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    recUdp()
    # sendUdp()
