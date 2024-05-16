import pigpio
import time


class servo44:

    def __init__(self): 
        # Gself.piO self.pin connected to the servo
        self.servoPinoDireita = 18
        self.servoPinoEsquerda = 17

        # Set servo parameters
        self.servo_min_pulse_width = 500  # in microseconds
        self.servo_max_pulse_width = 2500  # in microseconds
        self.servo_frequency = 50  # in Hz

        # Initialize pigpio
        self.pi = pigpio.pi()

        # Set servo pulse width range
        self.pi.set_servo_pulsewidth(self.pi.servo_gself.pio_self.pin, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)

    def controlarServo(self):
        try:
            while True:
                # Move servo to minimum position
                print("Moving to minimum position")
                self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_max_pulse_width)
                time.sleep(1)

                # Move servo to maximum position
                print("Moving to maximum position")
                self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_max_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nStopself.ping servo control")
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0)
            self.pi.stop()






if __name__ == "__main__":
    print("processo servo iniciado")
    servoclasse=servo44()
    servoclasse.controlarServo()