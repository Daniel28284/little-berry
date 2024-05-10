class faceTracking:
    def __init__(self):
        
        # Inicializa o classificador de faces do OpenCV, ou seja abre um modo de reconhecimento
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Cria uma instância da Picamera2
        picamera2 = Picamera2()

        # Configura a câmera, pode se quiser apagar as linhas 2 linhas abaixo
        config = picamera2.create_preview_configuration(main={"size": (500, 500), "format": "BGR888"})
        picamera2.configure(config)
        picamera2.start()

    try:
        while True:
            # Captura uma imagem diretamente em um array NumPy
            buffer = picamera2.capture_array()
            image = np.array(buffer, dtype=np.uint8)

            # Converte a imagem para tons de cinza para a detecção de faces
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detecta faces na imagem
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Desenha um retângulo em volta de cada face detectada e exibe suas coordenadas
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(image, f'({x}, {y})', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Exibe a imagem com as faces detectadas e suas coordenadas
            cv2.imshow("Camera", image)

            # Aguarda a tecla 'q' para sair
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cv2.destroyAllWindows()
        picamera2.stop()



if __name__ == "__main__":
    camera=faceTracking
    print("SOU O LITTLEB ERRY NO RASPBERRY")
	
    while True:
        # Captura uma imagem diretamente em um array NumPy
        buffer = picamera2.capture_array()
        image = np.array(buffer, dtype=np.uint8)

        # Converte a imagem para tons de cinza para a detecção de faces
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detecta faces na imagem
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Desenha um retângulo em volta de cada face detectada e exibe suas coordenadas
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, f'({x}, {y})', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Exibe a imagem com as faces detectadas e suas coordenadas
        cv2.imshow("Camera", image)

        # Aguarda a tecla 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
   