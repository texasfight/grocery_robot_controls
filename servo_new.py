from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from time import sleep

servo = Servo(12, pin_factory=PiGPIOFactory())

servo.min()
sleep(1)
servo.mid()
sleep(1)
servo.max()
sleep(1)

