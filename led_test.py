from gpiozero import LED
from time import sleep

led = LED(14)
led2 = LED(15)

led.blink(on_time=.2, off_time=.2)
sleep(5)
led2.blink(on_time=.2, off_time=.2)
sleep(2.4)
led.off()
sleep(2.6)
led2.off()

