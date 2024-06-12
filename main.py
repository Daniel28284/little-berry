import subprocess
from multiprocessing import Process
import time
import random
import os
import RPi.GPIO as GPIO




import BaseDados

import BaseDados
conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)

'''
        if GPIO.input(BUTTON_PIN_16) == GPIO.HIGH:
            print("pequeno")
            time.sleep(1)  # Add a delay to avoid multiple prints in a short time

        if GPIO.input(BUTTON_PIN_18) == GPIO.HIGH:
            print("Grande")
            time.sleep(1)  # Add a delay to avoid multiple prints in a short time

'''

BUTTON_small = 16
BUTTON_big = 18
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(BUTTON_small, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 16 to be an input pin with a pull-down resistor
GPIO.setup(BUTTON_big, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 18 to be an input pin with a pull-down resistor




def openMenu():
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair
    print("acabar def open menu")
    controldb.CONTROLanimacaoLeds=7
    controldb.CONTROLloopLeds=False
    controldb.CONTROLplayvideo=404 #meter o video do menu
    state = "HORAS"
    ciclo=True
    try:
        while ciclo:
            if state == "HORAS":
                controldb.CONTROLplayvideo=404 #meter o video do simbulo das horas
                if GPIO.input(BUTTON_big) == GPIO.HIGH:
                     # meter o video do simbulo das horas
                    state = "HORAS"
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    horas()

            elif state == "LUZ":
                controldb.CONTROLplayvideo=404 #meter o video do simbulo da luz
                if GPIO.input(BUTTON_small) == GPIO.HIGH:
                    state = "SHUTDOWN"
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    luz()

            elif state == "CRONOMETRO":
                if GPIO.input(BUTTON_small) == GPIO.HIGH:
                    state = "TIMER"
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    cronometro()

            elif state == "TIMER":
                if GPIO.input(BUTTON_small) == GPIO.HIGH:
                    state = "SHUTDOWN"
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    timer()

           
        
            time.sleep(0.1)  # Pequeno delay para debouncing
            #inatividade?

    except KeyboardInterrupt:
        GPIO.cleanup()                        

   
    

def horas():
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 
    print("acabar def horas")
    controldb.CONTROLplayvideo=404 #meter video da horas
    controldb.CONTROLanimacaoLeds=404 #meter um efeito tipo segundos
    



def luz():
    print("acabar def luz")
    controldb.CONTROLplayvideo=404 #meter video da luz
    controldb.CONTROLanimacaoLeds==8
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 


def shutdown():
    os.system("sudo shutdown now")

def cronometro():
    print("acabar def cronometro")
    #se clicar no botao A vai descendo o numero se clicar no B vai subindo 
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 

def timer():
    print("acabar def timer")
    #mm logica que o cronometro mas quando preciona a tecla B por 2 segundos comeca a contar
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 
     
    



def iniciar():
    #configdb.cor = 0
    #configdb.intensidadeDosLeds = 0.1
    controldb.CONTROLanimacaoLeds=5
    controldb.CONTROLloopLeds=True
    time.sleep(1000000000000000)
    controldb.CONTROLloopLeds=False


def inatividade():
    
    controldb.CONTROLplayvideo=1
    
   

    if(controldb.CONTROLanimacaoLeds!=configdb.animacaoInativo):
        controldb.CONTROLloopLeds=False
        controldb.CONTROLanimacaoLeds=configdb.animacaoInativo
        time.sleep(0.1)
        controldb.CONTROLloopLeds=True
        print("done")

    

    



def zangado():
    print("acabar def zagando")
  

    controldb.CONTROLplayvideo=404 #Animação feliz METER

    controldb.CONTROLanimacaoLeds=6

    for v in range(0,2):
        for i in range(500,2500,20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            print(i)
            time.sleep(0.0005)
        
        time.sleep(5)
    
        for i in range(2500,500, -20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            print(i)
            time.sleep(0.0005)


    
    
    




def feliz():
    
   

    controldb.CONTROLplayvideo=404 #Animação feliz METER

    controldb.CONTROLanimacaoLeds=6

    for v in range(0,2):
        for i in range(500,2500,20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            print(i)
            time.sleep(0.005)
        
        time.sleep(0)
    
        for i in range(2500,500, -20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            print(i)
            time.sleep(0.005)

    

    inatividade()
    




   




def erro(erro):
    '''
    erro: a mensagem a mostrar no terminal
    '''
    print(erro)
    controldb.CONTROLanimacaoLeds=404
    controldb.CONTROLloopLeds=True









# Função para executar um script com sudo -E env PATH=$PATH python3
def run_script(script_name, python_path='/usr/bin/python3'):
    command = ['sudo', '-E', 'env', f'PATH=$PATH', python_path, script_name]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Output of {script_name}:\n", result.stdout)
        print(f"Error (if any) of {script_name}:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command for {script_name} failed with return code {e.returncode}")
        print(f"Output of {script_name}:\n", e.stdout)
        print(f"Error of {script_name}:\n", e.stderr)

# Definir os scripts que serão executados como processos
SCRIPTS = [
    'Camera.py',
    'Leds.py',
    'servo.py',
    'player.py',
    'bluetooth.py'
]

if __name__ == '__main__':
    process_list = []

    # Caminho completo para o interpretador python3
    python_path = '/usr/bin/python3'  # Substitua pelo caminho retornado por `which python3`

    # Criar um processo para cada script
    for script in SCRIPTS:
        process_list.append(Process(target=run_script, args=(script, python_path)))

    # Iniciar todos os processos
    for p in process_list:
        p.start()






    

    time.sleep(4) #tempo para os processos iniciarem 

    while True:
        if GPIO.input(BUTTON_big) == GPIO.HIGH:
                print("BIG")
                openMenu()


        

        zangado()
    





    


