from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub() 
for i in range(0, 10, 2):
    hub.light_matrix.write(i)
    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep(100)
    hub.left_button.wait_until_released()
    hub.speaker.stop()

hub.light_matrix.show_image('HAPPY')
wait_for_seconds(1)
hub.speaker.start_beep(100)
hub.light_matrix.write('HAPPY')
hub.speaker.stop()
