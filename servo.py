import pigpio
import time

# GPIO pin connected to the servo
servo_gpio_pin = 18
servo_gpio_pin1 = 17

# Set servo parameters
servo_min_pulse_width = 500  # in microseconds
servo_max_pulse_width = 2500  # in microseconds
servo_frequency = 50  # in Hz

# Initialize pigpio
pi = pigpio.pi()

# Set servo pulse width range
pi.set_servo_pulsewidth(servo_gpio_pin, 0)
pi.set_servo_pulsewidth(servo_gpio_pin, servo_min_pulse_width)

try:
    while True:
        # Move servo to minimum position
        print("Moving to minimum position")
        pi.set_servo_pulsewidth(servo_gpio_pin, servo_min_pulse_width)
        pi.set_servo_pulsewidth(servo_gpio_pin1, servo_max_pulse_width)
        time.sleep(1)

        # Move servo to maximum position
        print("Moving to maximum position")
        pi.set_servo_pulsewidth(servo_gpio_pin, servo_max_pulse_width)
        pi.set_servo_pulsewidth(servo_gpio_pin1, servo_min_pulse_width)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping servo control")
    pi.set_servo_pulsewidth(servo_gpio_pin, 0)
    pi.stop()
