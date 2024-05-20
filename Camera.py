import cv2
import numpy as np
from picamera2 import Picamera2
import time
import pigpio
import BaseDados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)

# TODO: Adicionar o movimento do motor da base.


class faceTracking:
  
    def __init__(self):
        
        # Inicializa o classificador de faces do OpenCV, ou seja abre um modo de reconhecimento
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Cria uma instância da Picamera2
        self.picamera2 = Picamera2()

        # Configura a câmera, pode se quiser apagar as linhas 2 linhas abaixo
        self.config = self.picamera2.create_preview_configuration(main={"size": (500, 500), "format": "BGR888"})
        self.picamera2.configure(self.config)
        self.picamera2.start()
        self.NrDeLedsAcender = 0


        
    def teste(self):
        servo_gpio_pin = 18
        pi = pigpio.pi()
        posicaoAtual=500
        try:
            while controldb.CONTROLloopCamera :
                time.sleep(0) # possível controlar as frames por segundo pelo delay 
                # Captura uma imagem diretamente em um array NumPy
                buffer = self.picamera2.capture_array()
                image = np.array(buffer, dtype=np.uint8)

                # Converte a imagem para tons de cinza para a detecção de faces
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Detecta faces na imagem
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                # Desenha um retângulo em volta de cada face detectada e exibe suas coordenadas
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(image, f'({x}, {y})', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    print(x)
                    if x<110 : 
                        if posicaoAtual>500:
                            posicaoAtual=posicaoAtual-100
                            controldb.COntr
                            print("direita", posicaoAtual)
                    
                    if x>130 : 
                        if posicaoAtual<2500:
                            posicaoAtual=posicaoAtual+100
                            pi.set_servo_pulsewidth(servo_gpio_pin, posicaoAtual )
                            print("esquerda", posicaoAtual)

                # Exibe a imagem com as faces detectadas e suas coordenadas
                cv2.imshow("Camera", image)

                # Aguarda a tecla 'q' para sair
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cv2.destroyAllWindows()
            self.picamera2.stop()



if __name__ == "__main__":
    print("sou um teste da Camera")
    camera=faceTracking()  
    camera.teste()
      
	
	
