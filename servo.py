import pigpio
import time
import BaseDados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)


class servoClass:

    def __init__(self): 
        # definir os pinos para os pinos
        self.servoPinoDireita = 18
        self.servoPinoEsquerda = 17
        self.servoPinoMeio = 11 #olaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

        # definir o maximo e minimo do servo 
        self.servo_min_pulse_width = 500  # ms
        self.servo_max_pulse_width = 2500  # ms
        self.servo_frequency = 50  # Hz

        # inicar a biblioteca
        self.pi = pigpio.pi()

        # inicia os servos com 1
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)

        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)



    def teste(self):
            while True:   
                # Move o servo para o maximo e o minimo

                print("Moving to minimum position")
                self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_max_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_max_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoMeio, self.servo_max_pulse_width)
                time.sleep(3)

                print("Moving to maximum position")
                self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)
                self.pi.set_servo_pulsewidth(self.servoPinoMeio, self.servo_min_pulse_width)
                time.sleep(3)




    def controlarServo(self):
        posicaoDireita=int(500)
        posicaoEsquerda=int(500)
        posicaoMeio=int(500)
        try:
            while True:
                direitaDB=controldb.CONTROLservoDireita
                esquerdaDB=controldb.CONTROLservoEsquerda
                meioDB=controldb.CONTROLservoMeio
               

                if posicaoDireita!=direitaDB:
                    posicaoDireita=direitaDB
                    print("direita:", posicaoDireita)
                    self.pi.set_servo_pulsewidth(self.servoPinoDireita, int(posicaoDireita))

                if posicaoEsquerda!=esquerdaDB:
                    posicaoEsquerda=esquerdaDB
                    print("esquerda:", posicaoEsquerda)
                    self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, int(posicaoEsquerda))

               
                

             

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
    #servoclasse.teste()