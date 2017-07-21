import sys
import time
import subprocess
import os
from random import randint
from threading import Thread
from chippyRuxpin_audioPlayer import AudioPlayer
from chippyRuxpin_webFramework import WebFramework
import Adafruit_BBIO.GPIO as GPIO

enM = "P8_7"
enE = "P8_9"
MOUTH_OPEN = "P8_8"
MOUTH_CLOSE = "P8_10"
ain3Pin = "P8_12"
ain4Pin = "P8_14"

GPIO.setup(enM, GPIO.OUT)
GPIO.setup(enE, GPIO.OUT)
GPIO.setup(MOUTH_OPEN, GPIO.OUT)
GPIO.setup(MOUTH_CLOSE, GPIO.OUT)
GPIO.setup(ain3Pin, GPIO.OUT)
GPIO.setup(ain4Pin, GPIO.OUT)

GPIO.output(enM, GPIO.HIGH)
GPIO.output(enE, GPIO.HIGH)

audio = None
isRunning = True

def updateMouth():
    lastMouthEvent = 0
    lastMouthEventTime = 0

    while( audio == None ):
        time.sleep( 0.1 )
        
    while isRunning:
        if( audio.mouthValue != lastMouthEvent ):
            lastMouthEvent = audio.mouthValue
            lastMouthEventTime = time.time()

            if( audio.mouthValue == 1 ):
                GPIO.output( MOUTH_CLOSE, GPIO.LOW)
                GPIO.output( MOUTH_OPEN, GPIO.HIGH)
            else:
                GPIO.output( MOUTH_OPEN, GPIO.LOW)
                GPIO.output( MOUTH_CLOSE, GPIO.HIGH)
        else:
            if( time.time() - lastMouthEventTime > 0.4 ):
                GPIO.output( MOUTH_OPEN, 0 )
                GPIO.output( MOUTH_CLOSE, 0 )
