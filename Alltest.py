import websockets
import socket
import asyncio
import json
import time
from websockets import ConnectionClosed

port = 62436  # 设置端口号

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = ('127.0.0.1', 5679)  # 设置本地的端口，一般不写ip地址
udp_socket.bind(local_addr)  # 绑定套接字，不绑定端口号系统会随机分配

respond = {
    '702P': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    '705P': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    '710P_1': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    '710P_2': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    'walkIn_box': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    'saltSpray_box': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    'xenon_box': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    },
    'lowPressure_box': {
        'temperature': "0",
        'humidity': "0",
        'set_temperature': "0",
        'set_humidity': "0"
    }
}
machine_command_set: {
    'get_state': "S01#99#A",
    'temi_run': "E01#99#1#A",   # 格式：E01#99#1#A 说明：[01]是仪表的地址 [99]是查询指令 [1]表示启动运行
    'temi_stop': "E01#99#2#A",  # 格式：E01#99#2#A 说明：[01]是仪表的地址 [99]是查询指令 [2]表示停止运行

}


async def main(websocket):
    sendtext = "hello"  # 表示发送的内容
    udp_socket.sendto(sendtext.encode("utf-8"), ("127.0.0.1", 8887))
    frontinfo = await websocket.recv()
    print("front info : " + frontinfo)
    while True:
            recv_data = udp_socket.recvfrom(40960)  # 1024表示接收的最大的字节数，可以随意更改
            result_recv_data = recv_data[0].decode("utf-8")
            print(result_recv_data)
            respond['702P']['temperature'] = result_recv_data[0:2]
            respond['702P']['humidity'] = result_recv_data[2:4]
            respond['702P']['set_temperature'] = result_recv_data[4:6]
            respond['702P']['set_humidity'] = result_recv_data[6:8]

            json_str = json.dumps(respond['702P'])
            await websocket.send(json_str)
            await asyncio.sleep(2)



start_server = websockets.serve(main, '0.0.0.0', port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
