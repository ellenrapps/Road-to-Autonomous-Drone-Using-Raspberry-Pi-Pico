import hcsr04 #Import hcsr04 module written by Roberto Sanchez: https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py
import machine
from machine import UART
import utime


#Set UART channel and Baud rate
uart0 = UART(0, baudrate=115200)


#Function that reads serial data
def serial_read():
    recv=bytes()
    while uart0.any()>0:
        recv+=uart0.read(1)
    serial_recv=recv.decode('utf-8')
    return serial_recv


#Function that sends AT command to ESP01 via uart0
def AT_comm(cmd, uart=uart0, timeout=1000):
    print("CMD: " + cmd)
    uart.write(cmd)
    esp01_res(uart, timeout)
    print()
    
    
#Waiting time to get the response from ESP01
def esp01_res(uart=uart0, timeout=1000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)
        

#Configure to Factory Default Settings
AT_comm('AT+RESTORE\r\n')
utime.sleep(1)
print('Configure to Factory Default Settings')


#Configure as Soft Access Point (AP) Mode
AT_comm('AT+CWMODE=2\r\n')
utime.sleep(1)
print('Configure as AP mode')


#Configure as Multi Connections Mode
AT_comm('AT+CIPMUX=1\r\n') 
utime.sleep(1)
print('Configure as multi mode')


#Start server on Port 80
AT_comm('AT+CIPSERVER=1,80\r\n')
utime.sleep(1)
print('Configuration complete')


#Create an object using Sanchez hcsr04 module and class HCSR04 with parameters specifying the trigger pin and echo pin
sensor_pins = hcsr04.HCSR04(trigger_pin=19, echo_pin=26)


while True:
    #Distance calculation from Sanchez hcsr04 module is saved in variable distance_in_cm
    distance_in_cm = sensor_pins.distance_cm()
    
    #Code for HTML page display
    page_entry = '<head><title>Pico-Wifi-HCSR04</title></head><body><p><font size="+14">Obstacle Distance: '+str(int(distance_in_cm))+' cm'+'</p></body>'
    print(page_entry)
    length = str(len(page_entry))
    
    AT_comm = 'AT+CIPSEND=1,'+length
    uart0.write(AT_comm+'\r\n')
    utime.sleep(1)
    serial_recv = serial_read()
    print("Data sent-> "+serial_recv)
    AT_comm = page_entry
    uart0.write(AT_comm+'\r\n')
    utime.sleep(1)

