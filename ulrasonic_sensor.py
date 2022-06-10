import hcsr04 #Import hcsr04 module written by Roberto Sanchez: https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py  
import time #For delays
from machine import Pin, PWM #Import PIN, PWM from machine library   

sensor_pins = hcsr04.HCSR04(trigger_pin=19, echo_pin=26) #Create an object using Sanchez hcsr04 module and class HCSR04 with parameters specifying the trigger pin and echo pin   

#Passive Buzzer Control
passive_buzzer = PWM(Pin(18)) #Pin assignment for passive buzzer
passive_buzzer.freq(4186) #Set buzzer frequency
passive_buzzer.duty_u16(0) #Setting the duty_u16 to 0 ensures that when the machine is turned on, the buzzer won't immediately make a sound


while True:
    distance_in_cm = sensor_pins.distance_cm() #Distance calculation from Sanchez hcsr04 module is saved in variable distance_in_cm    
    print('Distance:', distance_in_cm, 'cm') #Print the distance in cm in the terminal
    
    if distance_in_cm <= 10: #If distance is less than or equal to 10 cm
        passive_buzzer.duty_u16(3500) #Passive buzzer makes some noise
    
    else: 
        passive_buzzer.duty_u16(0) #Passive buzzer stays silent
    
    time.sleep_ms(1000) #Delay by 1 second

