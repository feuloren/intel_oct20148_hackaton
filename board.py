import pyupm_grove
import pyupm_i2clcd
import pyupm_servo
import mraa

class PhysicalButton():
    def __init__(self, pin, default_handler = None):
        self.default_handler = default_handler
        
        self.button = mraa.Gpio(pin) # Hope we don't have to debounce...
        self.button.dir(mraa.DIR_IN)
        self.button.isr(mraa.EDGE_RISING, self.fire_click_callbacks)
        
        self.fire_on_click = []

    def do_once_on_click(self, callback):
        self.fire_on_click.append(("once", callback))

    def fire_click_callbacks(self):
        if self.fire_on_click:
            # Fire all the callback and remove the 'once' ones
            remaining_calls = []

            for registered in self.fire_on_click:
                registered[1]()
                if registered[0] == "always":
                    remaining_calls.append(registered)
                
            self.fire_on_click = remaining_calls
        elif self.default_handler:
            # Fire up the default handler if available
            self.default_handler()

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

    b.reset_alert_button = PhysicalButton(7)
    
    return b
