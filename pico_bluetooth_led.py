#import PIN and UART from machine library 
from machine import Pin, UART

#Define UART channel and Baud rate
uart1 = UART(0, 9600)

#Define GPIO Pin as LED output
led1 = Pin(17, Pin.OUT)

#Create an infinite loop
while True:
    if uart1.any(): #Check if data is available in UART channel
        receive = uart1.read() #If there is data in UART channel this will be saved in variable receive 
        receive = str(receive) #Data received is converted to string
        print(receive) #Print out the data received in the terminal
        
        if('ON' in receive): #If the text 'ON' is received 
            led1.value(1) #LED value is set to 1, turning the LED light on
           
        elif('OFF' in receive): #If the text "OFF" is received
            led1.value(0) # LED value is set to 0, turning the LED light off
       
