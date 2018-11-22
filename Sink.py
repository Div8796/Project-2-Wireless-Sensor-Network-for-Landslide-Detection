import serial
import time
import os
from socket import *
host = "192.168.43.224"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
ser = serial.Serial('COM3', 9600, timeout=0)
while 1:
    try:
        data=ser.readline()
        print(data)
        if(len(data)>14):
            UDPSock.sendto(data, addr)
        if data == "exit":
            break
        time.sleep(0.1)
    except ser.SerialTimeoutException:
        fo.write('Data could not be read')

