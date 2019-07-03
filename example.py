#!/usr/bin/python
import RPi.GPIO as GPIO
from tlc59711 import tlc59711

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
