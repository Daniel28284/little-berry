import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the servo
servo_pin = 18

# Set the PWM frequency (Hz)
pwm_frequency = 50

# Set the duty cycle ranges for the servo
duty_cycle_min = 1  # in percentage
duty_cycle_max = 85  # in percentage

# Initialize the GPIO pin for the servo
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize PWM for the servo
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Start PWM with initial duty cycle (servo at minimum position)
pwm.start(duty_cycle_min)

try:
    while True:
        # Prompt the user to enter a new duty cycle value
        new_duty_cycle = float(input("Enter a duty cycle value (1-85): "))
        
        # Check if the input value is within the valid range
        if duty_cycle_min <= new_duty_cycle <= duty_cycle_max:
            # Change the duty cycle
            pwm.ChangeDutyCycle(new_duty_cycle)
        else:
            print("Invalid duty cycle value. Please enter a value between 1 and 85.")

except KeyboardInterrupt:
    # Cleanup
    pwm.stop()
    GPIO.cleanup()
