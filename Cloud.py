import os
import re
from socket import *
from notify_run import Notify

host = ""
port = 13000
buf = 1024
addr = (host, port)
notify = Notify()

prev_gyrX=0 
prev_gyrY=0
prev_gyrZ=0
prev_accX=0
prev_accY=0
prev_accZ=0
gyr_X=0
gyr_Y=0
gyr_Z=0
acc_X=0
acc_Y=0
acc_Z=0
rain_data=0
moisture_data=0
high_rain=0
high_moisture=0
flag=0

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive data...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data=str(data)
    #print (data)
    if(data.find('rain data')!=-1):
        m = re.search('rain data = (.+?) ', data)
        if m:
            found = m.group(1)
        rain_data=int(found)
        print('Rain data = '+str(rain_data))
        if(rain_data>600):
            high_rain=0
    elif(data.find('moisture data')!=-1):
        m = re.search('moisture data = (.+?) ', data)
        if m:
            found = m.group(1)
        moisture_data=int(found)
        print('Moisture data = '+str(moisture_data))
        if(moisture_data>300):
            high_moisture=0
        if(moisture_data<300 and rain_data<600):
            high_moisture=1
            high_rain = 1
    elif(data.find('Accelerometer')!=-1):
        m = re.search('X = (.+?) ', data)
        if m:
            found = m.group(1)
        acc_X=int(found)
        m = re.search('Y = (.+?) ', data)
        if m:
            found = m.group(1)
        acc_Y=int(found)
        m = re.search('Z = (.+?) ', data)
        if m:
            found = m.group(1)
        acc_Z=int(found)
        print('Accelerometer Values Received => X = '+str(acc_X)+' ,  Y = '+str(acc_Y)+' ,  Z = '+str(acc_Z))
        if(abs(prev_accX-acc_X)>2000 or abs(prev_accY-acc_Y)>2000 or abs(prev_accZ-acc_Z)>2000):
            if(high_moisture and high_rain and flag==0):
                print('ALERT SENT')
                flag=1
                notify.send('LANDSLIDE ALERT')
        prev_accX=acc_X
        prev_accY=acc_Y
        prev_accZ=acc_Z   
    elif(data.find('Gyroscope')!=-1):
        m = re.search('X = (.+?) ', data)
        if m:
            found = m.group(1)
        gyr_X=int(found)
        m = re.search('Y = (.+?) ', data)
        if m:
            found = m.group(1)
        gyr_Y=int(found)
        m = re.search('Z = (.+?) ', data)
        if m:
            found = m.group(1)
        gyr_Z=int(found)
        print('Gyroscope Values Received => X = '+str(gyr_X)+' ,  Y = '+str(gyr_Y)+' ,  Z = '+str(gyr_Z))
        if(abs(prev_gyrX-gyr_X)>2000 or abs(prev_gyrY-gyr_Y)>2000 or abs(prev_gyrZ-gyr_Z)>2000):
            if(high_moisture and high_rain and flag==0):
                print('ALERT SENT')
                flag = 1
                notify.send('LANDSLIDE ALERT')
        prev_gyrX=gyr_X
        prev_gyrY=gyr_Y
        prev_gyrZ=gyr_Z
UDPSock.close()
os._exit(0)

