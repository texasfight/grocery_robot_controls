from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(.00001)

    GPIO.output(GPIO_TRIGGER, False)

    start = time.time()
    stop = time.time()
    
    while not GPIO.input(GPIO_ECHO):
        start = time.time()
    while GPIO.input(GPIO_ECHO):
        stop = time.time()
    
    elapsed = stop - start

    distance = elapsed * 34300 / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print(f"measured distance = {dist:.1f} cm")
            time.sleep(.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("All done")
