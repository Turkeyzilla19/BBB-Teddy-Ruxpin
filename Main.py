import sys
import time
import subprocess
import os
from random import randint
from threading import Thread
from Audio import AudioPlayer
import Adafruit_BBIO.GPIO as GPIO

words = raw_input("what words do you want? ")

subprocess.call(["espeak", "-w", "speech.wav", words, "-s", "130"])


enM = "P8_7"
enE = "P8_9"
MOUTH_OPEN = "P8_8"
MOUTH_CLOSE = "P8_10"
EYES_OPEN = "P8_12"
EYES_CLOSE = "P8_14"

GPIO.setup(enM, GPIO.OUT)
GPIO.setup(enE, GPIO.OUT)
GPIO.setup(MOUTH_OPEN, GPIO.OUT)
GPIO.setup(MOUTH_CLOSE, GPIO.OUT)
GPIO.setup(EYES_OPEN, GPIO.OUT)
GPIO.setup(EYES_CLOSE, GPIO.OUT)

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
                GPIO.output( MOUTH_OPEN, GPIO.LOW )
                GPIO.output( MOUTH_CLOSE, GPIO.LOW )
def updateEyes():
    while isRunning:
        GPIO.output( EYES_OPEN, GPIO.LOW)
        GPIO.output( EYES_CLOSE, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output( EYES_CLOSE, GPIO.LOW)
        GPIO.output( EYES_OPEN, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output( EYES_OPEN, GPIO.LOW)
        GPIO.output( EYES_CLOSE, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output( EYES_CLOSE, GPIO.LOW)
        GPIO.output( EYES_OPEN, GPIO.HIGH)
        time.sleep(randint( 0,7))

mouthThread = Thread(target=updateMouth)
mouthThread.start()
eyesThread = Thread(target=updateEyes)
eyesThread.start()     
audio = AudioPlayer()
audio.play("speech.wav")

        
