import cv2
import numpy as np
from picamera2 import Picamera2
import time
import pigpio
import BaseDados
import os


conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn)  # faz referência à base de dados das configurações
controldb = BaseDados.LittleBerryControl(conn)  # faz referência à base de dados de controle dos processos

# Classe responsável pela câmera e pelo reconhecimento facial
# Esta classe é executada em segundo plano e apenas é ativada a câmera se a classe main acioná-la
# Class com processos sensíveis: Não
# Proteção contra erros: Sim, caso a camara tenha algum problema
# Nível de Recursos utilizados: Muito alto
class FaceTracking:
  
    def __init__(self):
        
        try:
            # Inicializa o classificador de faces do OpenCV, ou seja, abre um modelo de reconhecimento
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Cria uma instância da Picamera2
            self.picamera2 = Picamera2()

            # Configura a câmera, pode apagar as 2 linhas abaixo se desejar MUDAR DEPOIS DE TESTAR
            self.config = self.picamera2.create_preview_configuration(main={"size": (500, 500), "format": "BGR888"})
            self.picamera2.configure(self.config)
            self.picamera2.start()

        except:
            print("camara mal conectada ou avarariada")
            


    def main(self):
        servo_gpio_pin = 27
        pi = pigpio.pi()
        posicaoAtual = 1500
        try:
            while True:
                cv2.destroyAllWindows()
                time.sleep(1)
                
                while controldb.CONTROLloopCamera:
                    time.sleep(0)  # possível controlar os frames por segundo pelo delay
                    # Captura uma imagem diretamente em um array NumPy
                    buffer = self.picamera2.capture_array()
                    image = np.array(buffer, dtype=np.uint8)

                    image = cv2.rotate(image, cv2.ROTATE_180)

                    # Converte a imagem para tons de cinza para a detecção de faces
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    # Detecta faces na imagem
                    faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                    # Desenha um retângulo em volta de cada face detectada e exibe suas coordenadas
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, f'({x}, {y})', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                        print(x)
                        # Faz atuar os servos conforme as coordenadas da face

                        if x < 110:  # se a face da pessoa estiver para a esquerda, a base deve virar para a direita
                            if posicaoAtual < 2500:
                                posicaoAtual += 10
                                pi.set_servo_pulsewidth(servo_gpio_pin, posicaoAtual)
                                print("direita", posicaoAtual)
                        
                        if x > 130:  # se a face da pessoa estiver para a direita, a base deve virar para a esquerda
                            if posicaoAtual > 500:
                                posicaoAtual -= 10
                                pi.set_servo_pulsewidth(servo_gpio_pin, posicaoAtual)
                                print("esquerda", posicaoAtual)
                                

                    # Exibe a imagem com as faces detectadas e suas coordenadas
                    cv2.imshow("Camera", image)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            cv2.destroyAllWindows()
            self.picamera2.stop()

if __name__ == "__main__":
    os.system("sudo pigpiod")
    # Inicia o main da câmera
    camera = FaceTracking()  
    camera.main()
