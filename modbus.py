# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     # ls = "36 56"
#     # print(ls[0:3])

import serial
from array import array
import os
import time

class modbus:

    # 定义基本属性
    comName = ""
    #定义私有属性,私有属性在类外部无法直接进行访问
    __tempSV = 0   # set temperature?
    __tempCV = 0   # current temperature?
    __humiSV = 0   # set humidity?
    __humiCV = 0   # current humidity?
    __stateV = 0
    __satempCV = 0
    __satempSV = 0
    __dstate = {        #用字典实现switch 功能
        0x00: '程式停止',
        0x01: '程式运行',
        0x02: '定值停止',
        0x03: '定值运行',
    }

    # def __init__(self, comName = "COM3"):      #构造方法
    #     comName = comName
    #     self.__serial = serial.Serial(comName, 2400)
    #     print(serial)
    #     if self.__serial.isOpen():
    #         print("打开串口成功")
    #     else:
    #         print("打开串口 failed")
    #
    # def __del__(self):
    #     if self.__serial != None:
    #         self.__serial.close()

    @staticmethod
    def __checkSum(self, array):    # 检查字符串
        if len(array) == 29:
            sum = 0
            temp = array[0:27]
            for b in temp:
                sum += b
            sum = 0x00ff & sum
            print('sum is:', sum, 'array[19] is:', array[27])
            if (sum == array[27]) and (sum == array[28]):
                return True
            else:
                return False
        return False

    def get_state(self):    # 获取机器当前状态
        cmd1 = b"S01#99#A"
        try:
            udp_socket.sendto(cmd1, ("192.168.3.7", 8887))
            data = udp_socket.recvfrom(40960)
            if __checkSum(data) is True:
                if self.__checkSum(self, data) is True:
                    self.__stateV = self.__dstate.get(data[2], '未知状态')
                    self.__tempCV = int.from_bytes(data[3:7], byteorder='little', signed=True) / 100
                    self.__tempSV = int.from_bytes(data[7:11], byteorder='little', signed=True) / 100
                    self.__humiCV = int.from_bytes(data[11:15], byteorder='little', signed=True) / 100
                    self.__humiSV = int.from_bytes(data[15:19], byteorder='little', signed=True) / 100
                    self.__satempCV = int.from_bytes(data[19:23], byteorder='little', signed=True) / 100
                    self.__satempSV = int.from_bytes(data[23:27], byteorder='little', signed=True) / 100
                    print(self.__stateV, 'TCV:', self.__tempCV, 'TSV:', self.__tempSV, ' ', self.__humiCV, ' ',
                          self.__humiSV, '', self.__satempCV, '', self.__satempCV)
                    # print('校验成功')
                else:
                    print('校验失败')
        except KeyboardInterrupt:
            # if self.__serial is not None:
            #     self.__serial.close()
            print("error")

    def temi_run(self):   # 运行设备
        cmd1 = b"E01#99#1#A"        #格式：E01#99#1#A 说明：[01]是仪表的地址 [99]是查询指令 [1]表示启动运行
        udp_socket.sendto(cmd1, ("192.168.3.7", 8887))
        data = udp_socket.recefrom(40960)
        print(data)
        # try:
        #     if self.__serial.is_open:
        #         self.__serial.write(cmd1)
        #     else:
        #         print('串口未打开或不存在')
        # except KeyboardInterrupt:
        #     if self.__serial is not None:
        #         self.__serial.close()

    def temi_stop(self):  # 停止设备
        cmd1 = b"E01#99#2#A"        #格式：E01#99#2#A 说明：[01]是仪表的地址 [99]是查询指令 [2]表示停止运行
        udp_socket.sendto(cmd1, ("192.168.3.7", 8887))
        data = udp_socket.recefrom(40960)
        print(data)
        # try:
        #     if self.__serial.is_open:
        #         self.__serial.write(cmd1)
        #     else:
        #         print('串口未打开或不存在')
        # except KeyboardInterrupt:
        #     if self.__serial is not None:
        #         self.__serial.close()

    def temi_set_temp(self, flaot):  # 设定温度
        """修改定值温度设定值"""
        cmd1 = b'E01#62#01#02' % (flaot)   #格式：E01#60#01#02修改值#A    例如:E01#600#478#56.24#A 把温度的设定值改为56.24  这个代码可能有点问题
        #cmd1 = bytes(str1,'ascii')
        print('修改定值温度设定值', cmd1)
        udp_socket.sendto(cmd1, ("192.168.3.7", 8887))
        data = udp_socket.recefrom(40960)
        print(data)
        # try:
        #     if self.__serial.is_open:
        #         self.__serial.write(cmd1)
        #     else:
        #         print('串口未打开或不存在')
        # except KeyboardInterrupt:
        #     if self.__serial is not None:
        #         self.__serial.close()

    def temi_set_humi(self, flaot):  # 设定湿度 代码可能有点问题
        """修改定值湿度设定值"""
        cmd1 = b'E01#60#02#02' % (flaot)  #格式：E01#60#02#02#修改值#A    例如:E01#600#479#90.0#A 把湿度的设定值改为90.0
        # cmd1 = bytes(str1,'ascii')
        print('修改定值湿度设定值',cmd1)
        udp_socket.sendto(cmd1, ("192.168.3.7", 8887))
        data = udp_socket.recefrom(40960)
        print(data)
        # try:
        #     if self.__serial.is_open:
        #         self.__serial.write(cmd1)
        #     else:
        #         print('串口未打开或不存在')
        # except KeyboardInterrupt:
        #     if self.__serial is not None:
        #         self.__serial.close()

    def displayState(self):    # 显示数据
        print('当前运行状态：',self.__stateV)
        return self.__stateV

    def displayTempCV(self):  # 显示当前实时温度
        print('当前实时温度：', self.__tempCV)
        return self.__tempCV

    def displayTempSV(self):  # 设置温度
        print('当前设置温度：', self.__tempSV)
        return self.__tempSV

    def displayHumiCV(self):  # 显示当前湿度
        print('当前实时湿度：', self.__humiCV)
        return self.__humiCV

    def displayHumiSV(self):  # 显示设定湿度？
        print('当前实时湿度：', self.__humiSV)
        return self.__humiSV

    def displaySatempCV(self):  # 显示当前饱和温度
        print('当前實時飽和溫度：', self.__satempCV)
        return self.__satempCV

    def displaySatempSV(self):  # 设置当前饱和温度
        print('当前設置飽和溫度：', self.__satempSV)
        return self.__satempSV
#
# temi880 = modbus("COM3")
# temi880.temi_run()
# time.sleep(2)
# # temi880.temi_set_temp(-39)
# # time.sleep(2)
# while True:
#     temi880.displayHumiCV()
#     temi880.displayHumiSV()
#     temi880.displayTempCV()
#     temi880.displayTempSV()
#     temi880.displayState()
#     temi880.displaySatempCV()
#     temi880.displaySatempSV()
#     temi880.get_state()
#
# print(temi880.__class__)
