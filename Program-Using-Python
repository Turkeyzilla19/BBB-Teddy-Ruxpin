import Adafruit_BBIO.GPIO as GPIO
from time import sleep 

enM = "P8_7"
enE = "P8_9"
ain1Pin = "P8_8"
ain2Pin = "P8_10"
ain3Pin = "P8_12"
ain4Pin = "P8_14"

GPIO.setup(enM, GPIO.OUT)
GPIO.setup(enE, GPIO.OUT)
GPIO.setup(ain1Pin, GPIO.OUT)
GPIO.setup(ain2Pin, GPIO.OUT)
GPIO.setup(ain3Pin, GPIO.OUT)
GPIO.setup(ain4Pin, GPIO.OUT)

GPIO.output(enM, GPIO.HIGH)
GPIO.output(enE, GPIO.HIGH)

while 1: 
  key = input("Press a key to change Teddy's facial features. ")
  if key == "w":
    GPIO.output(ain2Pin, GPIO.LOW)
    GPIO.output(ain1Pin, GPIO.HIGH)
    sleep(1.25)
    GPIO.output(ain1Pin, GPIO.LOW)
  elif key == "s":
    GPIO.output(ain1Pin, GPIO.LOW)
    GPIO.output(ain2Pin, GPIO.HIGH)
    sleep(1.25)
    GPIO.output(ain2Pin, GPIO.LOW)
  elif key == "a":
    GPIO.output(ain3Pin, GPIO.LOW)
    GPIO.output(ain4Pin, GPIO.HIGH)
    sleep(1.25)
    GPIO.output(ain4Pin, GPIO.LOW) 
  elif key == "d":
    GPIO.output(ain4Pin, GPIO.LOW)
    GPIO.output(ain3Pin, GPIO.HIGH)
    sleep(1.25)
    GPIO.output(ain3Pin, GPIO.LOW) 
