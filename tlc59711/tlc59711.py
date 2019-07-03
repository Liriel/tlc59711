#!/usr/bin/python
from time import sleep
import sys
import threading
import RPi.GPIO as GPIO

class tlc59711:
  def __init__(self, clkPin, datPin, numDrivers = 1, globalBrightness = 0x7F):
    # pins
    (self.__clk, self.__dat) = (clkPin, datPin)

    # flags
    self.__BCr = self.__BCg = self.__BCb = globalBrightness

    for p in ([self.__dat, self.__clk]):
      GPIO.setup(p, GPIO.OUT)

    # number of drivers
    self.__numDrivers = numDrivers

    # initialize PwmBuffer
    self.__pwmBuffer = [0x000 for i in range(0,12)]

  def _WriteMSB(self, d):

    b = 0x80
    # 12 bits per channel, send MSB first
    while b:
      GPIO.output(self.__clk, False)
      if (b & d):
        GPIO.output(self.__dat, True)
      else:
        GPIO.output(self.__dat, False)
      GPIO.output(self.__clk, True)
      b = b >> 1

  def _Write(self):
    cmd = 0x25
    cmd <<= 5
    cmd |= 0x16

    cmd <<= 7
    cmd |= self.__BCr
    cmd <<= 7
    cmd |= self.__BCb
    cmd <<= 7
    cmd |= self.__BCg

    for n in range(0, self.__numDrivers):
      self._WriteMSB(cmd >> 24)
      self._WriteMSB(cmd >> 16)
      self._WriteMSB(cmd >> 8)
      self._WriteMSB(cmd)

      # 12 channels per TLC59711
      for c in range(11, -1, -1):
        self._WriteMSB(self.__pwmBuffer[n*12 + c]>>8)
        self._WriteMSB(self.__pwmBuffer[n*12 + c])

    
  def _SetPWM(self, chan, pwm):
    if(chan > 12*self.__numDrivers): return
    self.__pwmBuffer[chan] = pwm

  def SetPWM(self, chan, pwm):
    self._SetPWM(chan, pwm)
    self._Write()

  def SetLED(self, lednum, r, g, b):
    self._SetPWM(lednum * 3, r)
    self._SetPWM(lednum * 3+1, g)
    self._SetPWM(lednum * 3+2, b)
    self._Write()
  
  def SetGlobalBrightness(self, brightness):
    if(brightness >= 0 and brightness <= 0x7F):
      self.__BCr = self.__BCg = self.__BCb = brightness
      self._Write()


# set pins to output mode
GPIO.setmode(GPIO.BCM)

tlc = tlc59711(23, 24)

chan = 0
print("Testing RGB LED")
tlc.SetLED(chan,0x0000, 0x0000, 0x0000)
sleep(.5)

print("Red")
tlc.SetLED(chan,0xFFFF, 0x0000, 0x0000)
sleep(1)

print("Green")
tlc.SetLED(chan,0x0000, 0xFFFF, 0x0000)
sleep(1)

print("Blue")
tlc.SetLED(chan,0x0000, 0x0000, 0xFFFF)
sleep(1)

print("Done")
tlc.SetLED(chan,0x0000, 0x0000, 0x0000)

print("Testing single channel")
tlc.SetPWM(chan,0xFFFF)
sleep(.5)
tlc.SetPWM(chan,0x0FFF)
sleep(.5)
tlc.SetPWM(chan,0x00FF)
sleep(.5)
print("Done")

print("Testing global brightness")
tlc.SetLED(chan,0x0000, 0xFFFF, 0x0000)
sleep(.5)
tlc.SetGlobalBrightness(0x5F)
tlc.SetLED(chan,0x0000, 0xFFFF, 0x0000)
sleep(.5)
tlc.SetGlobalBrightness(0x3F)
tlc.SetLED(chan,0x0000, 0xFFFF, 0x0000)
sleep(.5)
tlc.SetGlobalBrightness(0x0F)
tlc.SetLED(chan,0x0000, 0xFFFF, 0x0000)
sleep(.5)
print("Done")
tlc.SetLED(chan,0x0000, 0x0000, 0x0000)

GPIO.cleanup()
