from funcs import *
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM) #chip pin numbering
GPIO.setup(channel,GPIO.BOTH) #sets channel as output pin

def callback(channel):
    if GPIO.input(channel):
        print("LED is on")
    else:
        print("LED is off")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300) 
#       BOTH = detects High and Low events
#       bouncetime = minimum time between callbacks
GPIO.add_event_callback(channel,callback)
#       channel number will be passed to callback function

i = 0
while i<10:
    GPIO.output(17,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(17,GPIO.LOW)
    time.sleep(10)

    if i == 9:
        refillwater()
#end of loop
