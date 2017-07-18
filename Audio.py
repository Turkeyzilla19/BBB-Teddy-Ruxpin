import alsaaudio as aa
import audioop
from time import sleep
import struct
import math
import array
import numpy as np
import wave
import os
import subprocess

class AudioPlayer:
  def __init__(self):
    self.prevAudiovalue = 0
    self.mouthValue = 0
    
  def play(self,fileName):
