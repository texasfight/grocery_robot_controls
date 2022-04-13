import pigpio

servo = 12

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 50)

while True:
    duty = input("pulsewidth? ")
    if duty == "q":
        pwm.set_PWM_dutycycle(servo, 0)
        pwm.set_PWM_frequency(servo, 0)
        break

    pwm.set_servo_pulsewidth(servo, int(duty))
