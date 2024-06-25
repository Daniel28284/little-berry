import subprocess
from multiprocessing import Process
import time
import random
import os
import RPi.GPIO as GPIO

from datetime import datetime


import BaseDados
conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)


BUTTON_small = 16
BUTTON_big = 18
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(BUTTON_small, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 16 to be an input pin with a pull-down resistor
GPIO.setup(BUTTON_big, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 18 to be an input pin with a pull-down resistor




def openMenu():
    i=0 #variavel para p modo zangado
    click_big=False 
    lastButtonState = False
    debouncingTimer = 0
    print("acabar def open menu")
    controldb.CONTROLloopLeds=False
    controldb.CONTROLplayvideo=404 #meter o video do menu
    state = "HORAS"
    ciclo=True
    try:
        while ciclo:
            if state == "HORAS":
                controldb.CONTROLplayvideo=404 #meter o video do simbulo das horas
                if click_big:
                    click_big = False
                     # meter o video do simbulo das horas
                    state = "LUZ"
                    print("passou para luz")
                    i=i+1 #modo zangado
                    print("modo fun:",i)

                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    print("foi horas")
                    ciclo=False
                    horas()

            elif state == "LUZ":
                controldb.CONTROLplayvideo=404 #meter o video do simbulo da luz
                if click_big:
                    click_big = False
                    state = "SHUTDOWN"
                    print("passou para desligar")
                    i=i+1 #modo zangado
                    print("modo fun:",i)
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    luz()

            elif state == "SHUTDOWN":
                controldb.CONTROLplayvideo=404 #meter o video do simbulo da luz
                if click_big:
                    click_big = False
                    state = "CRONOMETRO"
                    print("passou para cronometro")
                    i=i+1 #modo zangado
                    print("modo fun:",i)
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    shutdown()

            elif state == "CRONOMETRO":
                if click_big:
                    click_big = False
                    state = "TIMER"
                    print("passou para timer")
                    i=i+1 #modo zangado
                    print("modo fun:",i)
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    cronometro()

            elif state == "TIMER":
                if click_big:
                    click_big = False
                    state = "CAMERA"
                    print("passou para Camera")
                    i=i+1 #modo zangado
                    print("modo fun:",i)
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    ciclo=False
                    timer()



            elif state == "CAMERA":
                if click_big:
                    click_big = False
                    state = "HORAS"
                    print("passou para Horas")
                    i=i+1 #modo zangado
                    print("modo fun:",i)
                elif GPIO.input(BUTTON_small) == GPIO.HIGH:
                    print("foi camera")
                    ciclo=False
                    camera()

            #modo zangado
            if i==20:
                print("acabar zangado no menu")
            
            if lastButtonState != GPIO.input(BUTTON_big):
                lastButtonState = GPIO.input(BUTTON_big)
                debouncingTimer = time.time()
                
            if time.time() - debouncingTimer > 0.1:
                click_big = lastButtonState
                debouncingTimer = time.time()

            

            time.sleep(0.1)  
            #inatividade?

    except KeyboardInterrupt:
        GPIO.cleanup()                        

   
    

def horas():
    
    now = datetime.now()
    before=99
    horas=now.hour
    minutos=now.minute
    print("tempo:", horas,minutos)
    
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 
    print("acabar def horas")

    
    
    time.sleep(0.5)
    ciclo=True
    while ciclo:
        now = datetime.now()
        if before!=now.minute:
            
            before=now.minute
            horas=now.hour
            minutos=now.minute
            print("tempo depois:", horas,minutos)


            if minutos<60 and horas<24:

                control = f"{horas:02d}_{minutos:02d}"
                controldb.CONTROLplayvideo=control
                print("control", control)

            

        if GPIO.input(BUTTON_small) == GPIO.HIGH:
            ciclo=False
            inatividade()
        
        time.sleep(0.1) 
       

   



def luz():
    print("acabar def luz")
    controldb.CONTROLplayvideo=404 #meter video da luz
    controldb.CONTROLloopLeds=True
    controldb.CONTROLanimacaoLeds=8
    

    
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair
   


def shutdown():
    os.system("sudo shutdown now")

 

def cronometro():
    print("acabar def timer")
    segundos =0 
    minutos= 0

    if GPIO.input(BUTTON_small) == GPIO.HIGH:
        inicio = time.time()
        while GPIO.input(BUTTON_small) == GPIO.HIGH:
            pass
        duracao = time.time() - inicio
        if duracao < 0.2:
            # Toque curto
            while True:
                #função pausa
                if GPIO.input(BUTTON_big) == GPIO.HIGH:
                    time.sleep(2)
                    while GPIO.input(BUTTON_big) == GPIO.LOW:
                        pass
                segundos=segundos+1
                
                #função sair
                if GPIO.input(BUTTON_small) == GPIO.HIGH:
                    break

                if segundos<61 and minutos<25:
                    if segundos==60:
                        segundos=0
                        minutos=minutos+1

                    control = f"{minutos:02d}_{segundos:02d}"
                    controldb.CONTROLplayvideo=control
                    print("control", control)
                time.sleep(1)
        inatividade()
    
        

           








    #mm logica que o cronometro mas quando preciona a tecla B por 2 segundos comeca a contar
    # tratar da logica de saida, que deve ser carregar muito tempo A para sair 
     
    
def timer():
    print("acabar def cronometro")
    minutosContar=0
    horas=0
    minutos=0
    ciclo=True
    while ciclo:
         
        if GPIO.input(BUTTON_small) == GPIO.HIGH:
            inicio = time.time()
            while GPIO.input(BUTTON_small) == GPIO.HIGH:
                pass
            duracao = time.time() - inicio
            if duracao < 0.2:
                # Toque curto
                minutos=minutos+1
                print("Toque curto: +1 minuto")
            minutosContar=minutosContar+1
            if minutos<60 and horas<24:
                
                if minutos==60:
                    minutos=0
                    horas=horas+1

                control = f"{horas:02d}_{minutos:02d}"
                controldb.CONTROLplayvideo=control
                print("control", control)
               

            elif duracao > 0.8:
                ciclo=False
                inatividade()
            

        if GPIO.input(BUTTON_big) == GPIO.HIGH:
            inicio = time.time()
            while GPIO.input(BUTTON_big) == GPIO.HIGH:
                pass
            duracao = time.time() - inicio
            if duracao < 0.2:
                # Toque curto
                minutos=minutos-1
                print("Toque curto: -1 minuto")

                if minutos>-1 and horas>-1:
                    minutosContar=minutosContar-1
                    if minutos==-1 and horas>0:
                        minutos=0
                        horas=horas-1
                        
                    control = f"{horas:02d}_{minutos:02d}"
                    controldb.CONTROLplayvideo=control
                    print("control", control)


            else:
                time.sleep(0.3)
                total_seconds = minutosContar
                start_time = time.time()
                while time.time() - start_time < total_seconds:
                    if GPIO.input(BUTTON_big) == GPIO.HIGH:
                        ciclo=False
                        print("Temporizador interrompido!")
                        inatividade()
                        
                    remaining_time = total_seconds - (time.time() - start_time)
                    mins, secs = divmod(remaining_time, 60)
                    timeformat = '{:02d}:{:02d}'.format(int(mins), int(secs))
                    print(timeformat, end='\r')
                    control = f"{int(mins):02d}_{int(secs):02d}"
                    controldb.CONTROLplayvideo=control

                    time.sleep(1)

                #acabou:
                ciclo=False
                controldb.CONTROLloopLeds=True
                controldb.CONTROLanimacaoLeds=5
                print("ola")
                while GPIO.input(BUTTON_small) == GPIO.LOW:
                    pass

                controldb.CONTROLloopLeds=False
                inatividade()





def camera():
    print("true1")
    controldb.CONTROLloopCamera=True
    print("true2")
    while GPIO.input(BUTTON_big) == GPIO.LOW:
        pass

    print("false1")
    controldb.CONTROLloopCamera=False
    print("false2")




   



def iniciar():
    #configdb.cor = 0
    #configdb.intensidadeDosLeds = 0.1
    controldb.CONTROLanimacaoLeds=5
    controldb.CONTROLloopLeds=True
    time.sleep(1000000000000000)
    controldb.CONTROLloopLeds=False


def inatividade():
    a=0
    ciclo=True
    controldb.CONTROLplayvideo=1
    '''
        if(controldb.CONTROLanimacaoLeds!=configdb.animacaoInativo):
            controldb.CONTROLloopLeds=False
            controldb.CONTROLanimacaoLeds=configdb.animacaoInativo
            time.sleep(0.1)
            controldb.CONTROLloopLeds=True
    '''

    while ciclo:
        if GPIO.input(BUTTON_big) == GPIO.HIGH:
            print("menu")
            ciclo=False
            openMenu()


        if configdb.notificacao==True:
            print("entrou aqui")
            controldb.CONTROLplayvideo=404 #Animação notificação METER
            controldb.CONTROLanimacaoLeds= configdb.estiloDosLedsNotificacao
            time.sleep(2)
            controldb.CONTROLanimacaoLeds=configdb.animacaoInativo
            controldb.CONTROLplayvideo=1



        if configdb.chamada==1:
            print("olaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            controldb.CONTROLplayvideo=6 #Animação notificação METER
            controldb.CONTROLanimacaoLeds= 5
            while GPIO.input(BUTTON_small) == GPIO.LOW:
                pass
            print("ola DEPOIS")
            controldb.CONTROLanimacaoLeds=configdb.animacaoInativo
            configdb.chamada=0
            
        time.sleep(0.1)
        
        
        #fazer alarmes se der tempo
                
        
           
        
    

    



def zangado():
    print("acabar def zagando")
  

    controldb.CONTROLplayvideo=404 #Animação  METER

    controldb.CONTROLanimacaoLeds=404

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
    
   

    controldb.CONTROLplayvideo= 4  #Animação feliz METER

    controldb.CONTROLanimacaoLeds=6

    for v in range(0,2):
        for i in range(500,2500,20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            time.sleep(0.005)
        
        time.sleep(0)
    
        for i in range(2500,500, -20):
            controldb.CONTROLservoDireita=int(i)
            controldb.CONTROLservoEsquerda=int(i)
            time.sleep(0.005)

    time.sleep(6)
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






    

    time.sleep(7) #tempo para os processos iniciarem 

    
    inatividade()



    





    


