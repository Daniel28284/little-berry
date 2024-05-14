import multiprocessing

#TODO: Criar base de dados redis com variaveis partilhadas
#TODO: Criar processo master que gerencia tudo
#TODO: Alterar cada codigo para receber comandos desta db 

PROCESSES = (
    FaceTracking,
    Leds,
    Servo,
    Master
)


if __name__ == "__main__":
    print("SOU O LITTLEB BERRY NO RASPBERRY")
    for p in PROCESSES:
        multipoc.ess.int(p)