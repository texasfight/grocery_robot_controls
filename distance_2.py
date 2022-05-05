from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

sensor = DistanceSensor(echo=5, trigger=6, pin_factory=PiGPIOFactory())
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
