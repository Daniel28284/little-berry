import serial

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
            decoded_output = serial_output.decode('utf-8')
            #Configura o descodificador para atuar conforme a norma utf-8
            cleaned_output = decoded_output.strip()
            #Faz atuar o codificador e guarda o resultado na variavel

            #Imprimir a mensagem
            print("mensgem recebida:", cleaned_output)
            return cleaned_output
            
        except Exception as e:
            print("Erro a receber a mensagem pedida, Provalmemte: socket/conexao fechada", e)
            return False
	
