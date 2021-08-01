from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike import DistanceSensor

hub = PrimeHub()
distance_sensor = DistanceSensor('C')

while True:
    distance_sensor.wait_for_distance_farther_than(10, 'in')
    hub.speaker.start_beep(70)
    distance_sensor.wait_for_distance_closer_than(10, 'in')
    hub.speaker.start_beep(85)
