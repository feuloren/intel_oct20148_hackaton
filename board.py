import pyupm_grove
import pyupm_i2clcd
import pyupm_servo
import mraa

def configure_board():
    "Set up the board sensors and actuators"
    
    class Board:
        pass
    b = Board()

    b.buzzer = mraa.Gpio(4)
    b.buzzer.dir(mraa.DIR_OUT)

    b.light = pyupm_grove.GroveLight(0) # b.value() for Lux, b.raw_value() for [0 - 1024] data
    b.temp = pyupm_grove.GroveTemp(1) # b.value() (celsius degrees ?)
    b.sound = mraa.Aio(2) # b.sound.read() [0 - 1024]

    b.lcd = pyupm_i2clcd.Jhd1313m1(0)
    
    return 
