import time
import thread
import math

from flask import Flask

from board import configure_board

app = Flask(__name__)

board = configure_board()

@app.route('/')
def home_route():
    return """<html>
<head><title></title></head>
<body>
    <p><a href="/beeps">Do some beeps</a></p>
    <p><a href="/room_data">Display room data</a></p>
    <p><a href="/redbutton">Red Button !</a></p>
</body>
</html>"""

def do_some_beeps(buzz):
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

@app.route('/beeps')
def beeps_route():
    thread.start_new_thread(do_some_beeps, (board.buzzer,))
    return "Beeps invasion launched"

@app.route('/room_data')
def current_data_route():
    # Read temperature, luminosity and sound intensity
    temp = board.temp.value()
    light = board.light.value()
    sound = board.sound.read() # Useless, we should capture data over a short period of time and return a mean
    return "Not yet"

@app.route('/redbutton')
def redbutton_route():
    # put the screen in red
    board.lcd.setColor(255, 0, 0)
    # Write scrolling ALERT
    # constant beep or SOS in Morse code with buzzer
    board.buzzer.write(1)
    return "Alert !!! Press button on device to stop"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6789)
