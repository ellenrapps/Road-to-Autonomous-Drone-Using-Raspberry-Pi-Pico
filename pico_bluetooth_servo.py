#import PIN, UART and PWM from machine library  
from machine import Pin, PWM, UART

#Define UART channel and Baud rate
uart1 = UART(0, 9600)

#Servo Number 1 control (PWM and Frequency)
servo1 = PWM(Pin(28))
servo1.freq(50)

#Servo Number 2 control (PWM and Frequency)
servo2 = PWM(Pin(27))
servo2.freq(50)

while True:
    if uart1.any(): #Check if data is available in UART channel
        receive = uart1.read() #If there is data in UART channel this will be saved in variable receive  
        receive = str(receive) #Data received is converted to string
        print(receive) #Print out the data received in the terminal 
        
        if('ON' in receive): #If the text 'ON' is received
            for duty in range(1000,9000,50): #Servos turn 180 degrees
                servo1.duty_u16(duty)
                servo2.duty_u16(duty)                
           
        elif('OFF' in receive): #If the text 'OFF' is received
            for duty in range(9000,1000,-50): #Servos turn 0 degree
                servo1.duty_u16(duty)
                servo2.duty_u16(duty)
