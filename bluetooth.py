import serial
import BaseDados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryConfig(conn)

class bluetooth:
	
    def __init__(self):
        self.ser = serial.Serial('/dev/rfcomm0')
        


    def referenciaSocket(self):
        try:
            # Cria uma variável "ser" e faz referência ao dispositivo que queremos comunicar
            self.ser = serial.Serial('/dev/rfcomm0')
            if self.ser.isOpen(): #Verifica se ha uma conexao retornado true ou false
                return self.ser
            else:
                print("Não foi possível abrir a porta serial.")
                return False
        except serial.SerialException as e:
            print("Erro ao abrir a porta serial:", e)
            return False
		

    def enviarMensagem(self,canal,mensagem):
        '''
        o canal é a variavel ser que vem de return do referenciaSocket
        '''
        try:
            mensagem_code= mensagem.encode('utf-8')
            canal.write(mensagem_code)
            return True
            
        except Exception as e:
            print("Erro ao enviar mensagem: Provalmemte: socket/conexao fechada", e)
            return False
        
		
    def lerMensagem(self,canal):
        '''
        o canal é a variavel ser que vem de return do referenciaSocket
        '''
        try:
            #esta linha serve para recolher o input a varivel NAO pode ser chamada de input
            iinput=self.ser.readline()

            #Decodificar os bytes vindos do bluetooth e guarda os na string
            decoded_output = iinput.decode('utf-8')
            #Configura o descodificador para atuar conforme a norma utf-8
            cleaned_output = decoded_output.strip()
            #Faz atuar o codificador e guarda o resultado na variavel

            #Imprimir a mensagem
            print("mensgem recebida:", cleaned_output)
            
            mensangemBruta=cleaned_output.split(";")
            intensidadeDosLeds, cor, horasDoAlarme1, nomeDoAlarme1, somDoAlarme1, estiloDosLeds1, horasDoAlarme2, nomeDoAlarme2, somDoAlarme2, estiloDosLeds2, horasDoAlarme3, nomeDoAlarme3, somDoAlarme3, estiloDosLeds3, chamada, nomeDaChamada, somDoToque, estiloDosLeds, notificacao, nomeDaNotificacao, conteudo, somDoToqueNotificacao, estiloDosLedsNotificacao =mensangemBruta


            
            db.intensidadeDosLeds = intensidadeDosLeds
            db.cor = cor
            db.horasDoAlarme1 = horasDoAlarme1
            db.nomeDoAlarme1 = nomeDoAlarme1
            db.somDoAlarme1 = somDoAlarme1
            db.estiloDosLeds1 = estiloDosLeds1
            db.horasDoAlarme2 = horasDoAlarme2
            db.nomeDoAlarme2 = nomeDoAlarme2
            db.somDoAlarme2 = somDoAlarme2
            db.estiloDosLeds2 = estiloDosLeds2
            db.horasDoAlarme3 = horasDoAlarme3
            db.nomeDoAlarme3 = nomeDoAlarme3
            db.somDoAlarme3 = somDoAlarme3
            db.estiloDosLeds3 = estiloDosLeds3
            db.chamada = chamada
            db.nomeDaChamada = nomeDaChamada
            db.somDoToque = somDoToque
            db.estiloDosLeds = estiloDosLeds
            db.notificacao = notificacao
            db.nomeDaNotificacao = nomeDaNotificacao
            db.conteudo = conteudo
            db.somDoToqueNotificacao = somDoToqueNotificacao
            db.estiloDosLedsNotificacao = estiloDosLedsNotificacao
            
            
            
            
            return cleaned_output
            
        except Exception as e:
            print("Erro a receber a mensagem pedida, Provalmemte: socket/conexao fechada", e)
            return False
        





if __name__ == "__main__":
    print("Sou um teste bluetooth")
    bluetooth0 = bluetooth()

    canal = bluetooth0.referenciaSocket()
    if canal != False:
        bluetooth0.enviarMensagem(canal, "eu sou um teste de bluetooth")
    else:
        print("Ligação com erro")

    print("Lendo o serial")
    bluetooth0.lerMensagem(canal)
    print("teste completo")