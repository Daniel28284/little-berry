import RPi.GPIO as GPIO
import time

# Define the GPIO pin numbers
c

# Set up GPIO
GPIO.setwarnings(False)  # Ignore warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(BUTTON_PIN_16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 16 to be an input pin with a pull-down resistor
GPIO.setup(BUTTON_PIN_18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 18 to be an input pin with a pull-down resistor

try:
    while True:  # Run forever
        if GPIO.input(BUTTON_PIN_16) == GPIO.HIGH:
            print("pequeno")
            time.sleep(1)  # Add a delay to avoid multiple prints in a short time

        if GPIO.input(BUTTON_PIN_18) == GPIO.HIGH:
            print("Grande")
            time.sleep(1)  # Add a delay to avoid multiple prints in a short time

except KeyboardInterrupt:
    pass  # If you press CTRL+C, exit the loop

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
