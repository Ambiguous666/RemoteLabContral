import websockets
import socket
import asyncio


# port = 62436  # 设置端口号


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = ('192.168.3.3', 5679)  # 设置本地的端口，一般不写ip地址
udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配


if __name__ == '__main__':
    sendtext = '01 03 010C 0002 05F4'  # 表示发送的内容
    udp_socket.sendto(bytes.fromhex(sendtext), ("192.168.3.7", 8887))
    recv_data = udp_socket.recvfrom(40960)  # 1024表示接收的最大的字节数，可以随意更改
    result_recv_data = recv_data[0]
    print(result_recv_data)
    print(result_recv_data.hex())
    # frontinfo = await websocket.recv()
    # print("front info : " + frontinfo)
    # t = 1000
    # while True:
    #     recv_data = udp_socket.recvfrom(4096)  # 1024表示接收的最大的字节数，可以随意更改
    #     result_recv_data = recv_data[0].decode("utf-8")
    #     print(result_recv_data)
    #     await websocket.send(result_recv_data)
    #     t = t-1
    #     await asyncio.sleep(1)
    # time.sleep(5)
    # udp_socket.close()


# start_server = websockets.serve(main, '0.0.0.0', port)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
