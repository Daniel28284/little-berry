import RPi.GPIO as GPIO
import time


class servoMotor:

    def __init__(self):
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(servoPIN, 50)  # 50Hz frequency
        self.p.start(0)



    def teste():
        try:
            while True:
                # Rotate from 0 to 180 degrees
                for angle in range(0, 181, 10):
                    duty_cycle = angle / 18 + 2
                    p.ChangeDutyCycle(duty_cycle)
                    time.sleep(0.5)

                # Rotate back from 180 to 0 degrees
                for angle in range(180, -1, -10):
                    duty_cycle = angle / 18 + 2
                    p.ChangeDutyCycle(duty_cycle)
                    time.sleep(0.5)

        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()
