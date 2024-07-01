import serial
import BaseDados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn)  # faz referência à base de dados das configurações
controldb = BaseDados.LittleBerryConfig(conn) # faz referência à base de dados de controle dos processos 





# Classe responsável pela coleta, filtragem e armazenamento de dados. 
# Esta classe executa em segundo plano e seu funcionamento não é controlado pela classe main, 
# Esta executa  até o encerramento do robô.
# Class com processos sensíveis: Sim
# Proteção contra erros: Sim
# Nível de Recursos utilizados: Baixo
class bluetooth:
	
    def __init__(self):
        print("ola")
        #self.ser = serial.Serial('/dev/rfcomm0')  # encontra o dispositivo para comunicar, neste caso o raspberry

    def referenciaSocket(self):
        # método que verifica e atualiza a referência ao socket do bluetooth para comunicar com o raspberry, como é um método sensível, tem funções try e tratamento de erros
        try:
            # Cria uma variável "ser" e faz referência ao dispositivo que queremos comunicar
            self.ser = serial.Serial('/dev/rfcomm0')
            if self.ser.isOpen(): # Verifica se há uma conexão retornando true ou false
                return self.ser
            else:
                self.referenciaSocket()
                print("Não foi possível abrir a porta serial.")
                
                
        except serial.SerialException as e:
            self.referenciaSocket()
            print("Erro ao abrir a porta serial:", e)
            
		
    def enviarMensagem(self, canal, mensagem):
        # método que permite enviar informações do bluetooth para o raspberry, como é um método sensível, tem funções try e tratamento de erros
        '''
        canal = variável ser que vem de return da referenciaSocket
        '''
        try:
            mensagem_code = mensagem.encode('utf-8')
            canal.write(mensagem_code)
            return True
            
        except Exception as e:
            self.referenciaSocket()
            print("Erro ao enviar mensagem: Provavelmente: socket/conexão fechada", e)
            
        
    def lerMensagem(self, canal):
        # método que permite receber a trama de dados do bluetooth vinda do raspberry com o objetivo de filtrar e guardar na base de dados, como é um método sensível, tem funções try e tratamento de erros
        '''
        o canal é a variável ser que vem do return do referenciaSocket
        '''
        try:
            # esta linha serve para recolher o input, a variável NÃO pode ser chamada de input, porque input é uma palavra reservada
            iinput = self.ser.readline()

            # Decodificar os bytes vindos do bluetooth e guardá-los na string
            decoded_output = iinput.decode('utf-8')
            # Configura o decodificador para atuar conforme a norma utf-8
            cleaned_output = decoded_output.strip()
            # Faz atuar o codificador e guarda o resultado na variável

            # Imprimir a mensagem
            print("mensagem recebida:", cleaned_output)

            # começa o processo de filtragem onde se sabe que cada informação é separada por ponto e vírgula
            mensagemBruta = cleaned_output.split(";") # separa as informações com o critério do ponto e vírgula
            intensidadeDosLeds, cor, horasDoAlarme1, nomeDoAlarme1, somDoAlarme1, estiloDosLeds1, horasDoAlarme2, nomeDoAlarme2, somDoAlarme2, estiloDosLeds2, horasDoAlarme3, nomeDoAlarme3, somDoAlarme3, estiloDosLeds3, chamada, nomeDaChamada, somDoToque, estiloDosLeds, notificacao, nomeDaNotificacao, conteudo, somDoToqueNotificacao, estiloDosLedsNotificacao, animacaoInativo = mensagemBruta
            # as informações filtradas são guardadas em diferentes variáveis

            # é passado o valor dentro das variáveis para a base de dados para serem acessadas por todas as classes
            configdb.intensidadeDosLeds = float(intensidadeDosLeds)
            configdb.cor = int(cor)
            configdb.horasDoAlarme1 = horasDoAlarme1
            configdb.nomeDoAlarme1 = nomeDoAlarme1
            configdb.somDoAlarme1 = somDoAlarme1
            configdb.estiloDosLeds1 = estiloDosLeds1
            configdb.horasDoAlarme2 = horasDoAlarme2
            configdb.nomeDoAlarme2 = nomeDoAlarme2
            configdb.somDoAlarme2 = somDoAlarme2
            configdb.estiloDosLeds2 = estiloDosLeds2
            configdb.horasDoAlarme3 = horasDoAlarme3
            configdb.nomeDoAlarme3 = nomeDoAlarme3
            configdb.somDoAlarme3 = somDoAlarme3
            configdb.estiloDosLeds3 = estiloDosLeds3
            configdb.chamada = int(chamada)
            configdb.nomeDaChamada = nomeDaChamada
            configdb.somDoToque = somDoToque
            configdb.estiloDosLeds = estiloDosLeds
            configdb.notificacao = notificacao
            configdb.nomeDaNotificacao = nomeDaNotificacao
            configdb.conteudo = conteudo
            configdb.somDoToqueNotificacao = somDoToqueNotificacao
            configdb.estiloDosLedsNotificacao = estiloDosLedsNotificacao
            configdb.animacaoInativo = int(animacaoInativo)

            # print para debug
            print("dados recebidos:", intensidadeDosLeds, cor, horasDoAlarme1, nomeDoAlarme1, somDoAlarme1, estiloDosLeds1, horasDoAlarme2, nomeDoAlarme2, somDoAlarme2, estiloDosLeds2, horasDoAlarme3, nomeDoAlarme3, somDoAlarme3, estiloDosLeds3, "chamada: ", chamada, nomeDaChamada, somDoToque, estiloDosLeds, notificacao, nomeDaNotificacao, conteudo, somDoToqueNotificacao, estiloDosLedsNotificacao)
            
            if configdb.chamada==1:
                print("chamada aqui")


            return cleaned_output
            
        except Exception as e:
            self.referenciaSocket()
            print(e)
            print("Erro ao receber a mensagem pedida, provavelmente: socket/conexão fechada", e)
            


if __name__ == "__main__":
    # método chamado quando esta classe é referida 

    bluetooth0 = bluetooth()
    canal = bluetooth0.referenciaSocket()

    # fica em loop buscando dados do bluetooth
    while True:
        bluetooth0.lerMensagem(canal)
