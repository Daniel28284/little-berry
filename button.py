import RPi.GPIO as GPIO
import time

# Classe usada apenas para testar os botões 

# Configura o GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(BUTTON_PIN_16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Define o pino 16 como entrada com uma resistência pull-down
GPIO.setup(BUTTON_PIN_18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Define o pino 18 como entrada com uma resistência pull-down

try:
    while True:  
        if GPIO.input(BUTTON_PIN_16) == GPIO.HIGH:
            print("Pequeno")
            time.sleep(1)  # Delay para dar tempo do botão voltar ao lugar e não acionar várias vezes

        if GPIO.input(BUTTON_PIN_18) == GPIO.HIGH:
            print("Grande")
            time.sleep(1)  # Delay para dar tempo do botão voltar ao lugar e não acionar várias vezes

except KeyboardInterrupt:
    pass  

finally:
    GPIO.cleanup()  
