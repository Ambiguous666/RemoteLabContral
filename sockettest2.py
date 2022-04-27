import websockets
import socket
import asyncio
import time

port = 7788  # 设置端口号
'''
前端发送string类型的json对象：{“requestType”:requestValue}
requestValue={"key":"value","key","value"}
'''



def recUdp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字，ipv4，UDP类型
    local_addr = ('192.168.3.3', 5679)  # 设置本地的端口，一般不写ip地址
    udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配

    recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改
    # result_recv_data = recv_data[0].hex()  # 接收的数据类型为Hex
    result_recv_data = recv_data[0].decode('utf-8')
    # 3.关闭套接字
    udp_socket.close()
    return result_recv_data


def sendUdp():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sendtext = "hello"  # 表示发送的内容
    # udp_socket.sendto("发送的内容".encode("编码格式"), ("目的ip", "目的端口号"))
    udp_socket.sendto(sendtext.encode("utf-8"), ("192.168.3.7", 8887))

    # 3.关闭套接字
    udp_socket.close()


async def main(websocket):
    frontInfo = await websocket.recv()  # 等待前端发送信息,string类型
    print("front mssage:" + frontInfo)
    response = "25446677"
    print("respond to front:" + response)
    await websocket.send(response)
    while True:
        ls = recUdp()
        print(ls)
        await websocket.send(ls)


# if __name__ == "__main__":  # 可运行版本
#     # sendUdp()
#     # while True:
#     #     ls = recUdp()
#     #     print(ls)
#     # 1.创建一个udp套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # udp_socket.sendto("发送的内容".encode("编码格式"), ("目的ip", "目的端口号"))
#
#     local_addr = ('192.168.3.3', 5679)  # 设置本地的端口，一般不写ip地址
#     udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配
#     sendtext = "hello"  # 表示发送的内容
#     udp_socket.sendto(sendtext.encode("utf-8"), ("192.168.3.7", 8887))
#     while True:
#         recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改
#         result_recv_data = recv_data[0].decode('utf-8')
#         print(result_recv_data)

# if __name__ == "__main__":
#     # sendUdp()
#     # while True:
#     #     ls = recUdp()
#     #     print(ls)
#     # 1.创建一个udp套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # udp_socket.sendto("发送的内容".encode("编码格式"), ("目的ip", "目的端口号"))
#
#     local_addr = ('192.168.3.3', 5679)  # 设置本地的端口，一般不写ip地址
#     udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配
#     sendtext = "hello"  # 表示发送的内容
#     udp_socket.sendto(sendtext.encode("utf-8"), ("192.168.3.7", 8887))
#     while True:
#         recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改
#         result_recv_data = recv_data[0].decode('utf-8')
#         print(result_recv_data)



# start_server = websockets.serve(main, '0.0.0.0', port)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
