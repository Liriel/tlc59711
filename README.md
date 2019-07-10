# tlc59711 12 channel LED PWM driver

python port of the c++ version by adafruit https://github.com/adafruit/Adafruit_TLC59711

## Chip

Datasheet: http://www.ti.com/lit/ds/symlink/tlc59711.pdf
Adafruit prototyping board: https://www.adafruit.com/product/1455

One communicates with the chip via the i2c bus by toggling clk (clock) to shift the current state (low/high) of the data pin into the ICs 16bit register.

## Usage

Connect the IC to your pi using any two GPIO pins

| Name   | RPi Pin | RPi GPIO | TLC59711 | Adafruit TLC59711 |
| ------ | ------: | -------- | -------- | ----------------- |
| Data   |      18 | GPIO24   | SDTI     | DI                |
| Clock  |      16 | GPIO23   | SCKI     | CI                |
| 3v3    |       1 | 3v3      | 3v3      | VCC               |
| Ground |       6 | GND      | GND      | GND               |

import the library and RPi.GPIO

    import RPi.GPIO as GPIO
    from tlc59711 import tlc59711

    GPIO.setmode(GPIO.BCM)
    tlc = tlc59711(23, 24)

now you can set each channel like this

    tlc.SetPWM(0,0xFFFF)

this sets channel 0 to maximum brightness. The TLC supports 65536 brightness steps from 0 to 100%:

| Value  | Brightness |
| ------ | ---------: |
| 0xFFFF |       100% |
| 0x7FFF |        50% |
| 0x3FFF |        25% |

the datasheet has more information on this

## License

this package is a port of https://github.com/adafruit/Adafruit_TLC59711 their BSD license.txt is included in this repository.
