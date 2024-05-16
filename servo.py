import pigpio
import time


class servoClass:

    def __init__(self): 
        # Gself.piO self.pin connected to the servo
        self.servoPinoDireita = 18
        self.servoPinoEsquerda = 17
        self.servoPinoMeio = 11 #olaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

        # Set servo parameters
        self.servo_min_pulse_width = 500  # in microseconds
        self.servo_max_pulse_width = 2500  # in microseconds
        self.servo_frequency = 50  # in Hz

        # Initialize pigpio
        self.pi = pigpio.pi()

        # Set servo pulse width range
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)

        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)



    def teste(self):
        # Move servo to minimum position
            print("Moving to minimum position")
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_max_pulse_width)
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_max_pulse_width)
            self.pi.set_servo_pulsewidth(self.servoPinoMeio, self.servo_max_pulse_width)
            time.sleep(1)

            # Move servo to maximum position
            print("Moving to maximum position")
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)
            self.pi.set_servo_pulsewidth(self.servoPinoMeio, self.servo_min_pulse_width)
            time.sleep(1)




    def controlarServo(self):
        try:
            while True:
                direitaDB=db.CONTROLservoDireita
                esquerdaDB=db.CONTROLservoEsquerda
                meioDB=db.CONTROLservoMeio
                posicaoDireita=500
                posicaoEsquerda=500
                posicaoMeio=500

                if posicaoDireita!=direitaDB:
                    posicaoDireita=direitaDB
                    self.pi.set_servo_pulsewidth(self.servoPinoDireita, posicaoDireita)

                if posicaoEsquerda!=esquerdaDB:
                    posicaoEsquerda=esquerdaDB
                    self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, posicaoEsquerda)

                if posicaoMeio!=meioDB:
                    posicaoMeio=meioDB
                    self.pi.set_servo_pulsewidth(self.servoPinoMeio, posicaoMeio)
                

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
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)
            self.pi.set_servo_pulsewidth(self.servoPinoMeio, 0)
            self.pi.stop()






if __name__ == "__main__":
    print("processo servo iniciado")
    servoclasse=servoClass()
    servoclasse.controlarServo()