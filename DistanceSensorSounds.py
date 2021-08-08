from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike import DistanceSensor

hub = PrimeHub()
distance_sensor = DistanceSensor('C')

# Beep: 44 to 123 ("60" is the middle C note)
# Distance get_distance_inches() 0-79

while True:
    distance = distance_sensor.get_distance_inches()
    if (distance is not None):
        note = int(distance + 70)
        hub.light_matrix.write(note)
        wait_for_seconds(0.5)
        hub.speaker.start_beep(note)
