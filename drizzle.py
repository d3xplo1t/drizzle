#Drizzle v0.1 09/2022

import RPi.GPIO as gp
import time

#Setting pins.
#PIN11(GPIO017) = RELAY

time.sleep(10)

while (True):
    gp.setmode(gp.BOARD)
    gp.setup(11, gp.OUT)
    print("Drizzle time, pump activated!")
    time.sleep(2)
    gp.cleanup()
    #live terminal countdown
    for i in range(80000,0,-1):
        print(f"{i}", end="\r", flush=True)
        time.sleep(1)

