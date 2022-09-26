#Drizzle v0.1 09/2022

import RPi.GPIO as GPIO
import time

#Setting pins.
#PIN4 = HUMIDITY SENSOR
#PIN11 = RELAY

gp.setmode(GPIO.BCM)
gp.setup(4, GPIO.OUT) #humidity sensor
gp.setup(11, GPIO.OUT) #relay


try:
    while True:
        if (GPIO.input(4))==0:
            print("Wet")
        elif (GPIO.input(4))==1:
            print("Dry") and gp.output(11, GPIO.HIGH)
            time.sleep(2)
            print("Drizzle time!!")
            GPIO.cleanup()
        time.sleep(3600)

#clean the GPIO pins before endings

finally:
    GPIO.cleanup()



