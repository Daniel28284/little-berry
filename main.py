import subprocess
from multiprocessing import Process
import time




import BaseDados

import BaseDados
conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)








def iniciar():
    configdb.cor = 1
    configdb.intensidadeDosLeds = 1
    controldb.CONTROLanimacaoLeds=5
    controldb.CONTROLloopLeds=True
    time.sleep(2)
    controldb.CONTROLloopLeds=False










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


    iniciar()





    


