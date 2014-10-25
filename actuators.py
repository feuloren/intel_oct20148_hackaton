import time
import math

import pyupm_i2clcd
led = pyupm_i2clcd.Jhd1313m1(0)
lcd.setColor(254,0,0)
led.setCursor(0,0)
led.write('15 C - 70dB')
led.setCursor(1,3)
led.write('Everything ok')
led.clear()

def var_backlight(fun = math.sin, delay=0.1, incr_to_max = 100):
    for i in range(2 * incr_to_max):
        angle = math.pi / (2 * incr_to_max) * i
        print angle, int(fun(angle) * 255)
        lcd.setColor(int(fun(angle) * 255),0,0)
        time.sleep(0.1)

import pyupm_servo
servo = pyupm_servo.ES08A(3)

import mraa
led = mraa.Gpio(6)
led.dir(mraa.DIR_OUT)
led.write(1)
led.write(0)

import thread

buzz = mraa.Gpio(4)
buzz.dir(mraa.DIR_OUT)
def do_some_beeps():
    buzz.write(1)
    time.sleep(0.1)
    buzz.write(0)
    time.sleep(0.1)
    buzz.write(1)
    time.sleep(0.2)
    buzz.write(0)
    time.sleep(0.05)
    buzz.write(1)
    time.sleep(0.1)
    buzz.write(0)

thread.start_new_thread(do_some_beeps, ())
