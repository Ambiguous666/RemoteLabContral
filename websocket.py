import websockets
import socket
import asyncio

port = 5679  # 设置端口号
'''
前端发送string类型的json对象：{“requestType”:requestValue}
requestValue={"key":"value","key","value"}
'''

async def main(websocket):
    frontInfo = await websocket.recv()  # 等待前端发送信息,string类型
    print("front mssage:" + frontInfo)
    response = "25"
    print("respond to front:" + response)
    await websocket.send(response)
    ls = "潮湿"
    await websocket.send(ls)


start_server = websockets.serve(main, '0.0.0.0', port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
