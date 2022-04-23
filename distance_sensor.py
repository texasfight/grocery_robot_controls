from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 3
GPIO_ECHO = 2

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():

    # Set off trigger to start measuring
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Initialize timer variables
    start = time.time()
    stop = time.time()
    
    # Loop for setting start time
    while not GPIO.input(GPIO_ECHO):
        start = time.time()

    # Loop to set stop time
    while GPIO.input(GPIO_ECHO):
        stop = time.time()
    
    # Calculate time difference
    elapsed = stop - start

    # Calculate distance based on elapsed time and speed of waves.
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
