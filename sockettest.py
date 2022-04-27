import websockets
import socket
import asyncio
import time
import glabalVal as g

temperature = "25"
humidity = "44"

def recUdp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字，ipv4，UDP类型
    local_addr = ("", 62436)  # 设置本地的端口，一般不写ip地址
    udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配

    recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改
    result_recv_data = recv_data[0].hex()  # 接收的数据类型为Hex

    str = result_recv_data
    # 3.关闭套接字
    udp_socket.close()
    return str


if __name__ == '__main__':
    while True:
        info = recUdp()
        print(info)
        g.set_temeperature(info[0:4])
        g.set_humidity(info[4:16])
        print(g.get_temperature())
        print(g.get_humidity())
        time.sleep(2)




