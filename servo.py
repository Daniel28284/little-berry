import pigpio
import time
import BaseDados


conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)

# Classe responsável por controlar os servos no braço do robô
# Esta classe é executada em segundo plano e recebe comandos da class main
# Processos sensíveis: Não
# Proteção contra erros: Sim
# Nível de recursos utilizados: Baixo a Médio
class servoClass:
    
    def __init__(self):
        
         # Este comando precisa ser executado para que a biblioteca funcione como esperado.

        # Define os pinos para cada um dos servos.
        self.servoPinoDireita = 18
        self.servoPinoEsquerda = 17

        # Define o máximo e mínimo de largura de pulso para os servos, e a frequência dos servos.
        self.servo_min_pulse_width = 500  # microssegundos
        self.servo_max_pulse_width = 2500  # microssegundos
        self.servo_frequency = 50  # Hz

        # Inicia a biblioteca pigpio.
        self.pi = pigpio.pi()

        # Inicializa os servos com 0 (sem força) e depois posiciona a 0 graus.
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)
        self.pi.set_servo_pulsewidth(self.servoPinoDireita, self.servo_min_pulse_width)
        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, self.servo_min_pulse_width)
        time.sleep(1)
        

    # Este método roda em loop e ajusta os servos quando detecta uma diferença na posição desejada.
    def controlarServo(self):
        controldb.CONTROLservoEsquerda=500
        controldb.CONTROLservoDireita = 500
        posicaoDireita = int(500)
        posicaoEsquerda = int(500)

        try:
            while True:
                direitaDB = controldb.CONTROLservoDireita
                esquerdaDB = controldb.CONTROLservoEsquerda

                if posicaoDireita != direitaDB:
                    posicaoDireita = direitaDB
                    print("Posição direita atualizada:", posicaoDireita)
                    self.pi.set_servo_pulsewidth(self.servoPinoDireita, int(3000 - posicaoDireita))

                if posicaoEsquerda != esquerdaDB:
                    posicaoEsquerda = esquerdaDB
                    print("Posição esquerda atualizada:", posicaoEsquerda)
                    self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, int(posicaoEsquerda))

                time.sleep(0.1)  # Pequeno delay para otimização do codigo

        except Exception as e:
            print("Erro ao controlar os servos:", str(e))
            # Libera os servos em caso de erro.
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0) 
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)



        self.pi.set_servo_pulsewidth(self.servoPinoDireita, 0) 
        self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, 0)


    
    def teste(self):
        while True:
            posi=2500
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, posi)
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, posi)
            time.sleep(1)
            posi=500
            self.pi.set_servo_pulsewidth(self.servoPinoDireita, posi)
            self.pi.set_servo_pulsewidth(self.servoPinoEsquerda, posi)
            time.sleep(1)


if __name__ == "__main__":
   

    servoclasse = servoClass()
    servoclasse.controlarServo()
    time.sleep(0.2)


