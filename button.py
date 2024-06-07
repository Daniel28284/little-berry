import RPi.GPIO as GPIO
import time

# Define the GPIO pin numbers
BUTTON_PIN_16 = 16
BUTTON_PIN_18 = 18

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(BUTTON_PIN_16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin 16 as an input with a pull-up resistor
GPIO.setup(BUTTON_PIN_18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin 18 as an input with a pull-up resistor

# Define a callback function to run when the button is pressed
def button_callback(channel):
    if channel == BUTTON_PIN_16:
        print("Button on pin 16 pressed!")
    elif channel == BUTTON_PIN_18:
        print("Button on pin 18 pressed!")

# Add event detection for both buttons
GPIO.add_event_detect(BUTTON_PIN_16, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(BUTTON_PIN_18, GPIO.FALLING, callback=button_callback, bouncetime=300)

print("Press the buttons connected to GPIO pins 16 and 18. Press Ctrl+C to exit.")

try:
    # Keep the script running to monitor button presses
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    print("Exiting...")
    GPIO.cleanup()
