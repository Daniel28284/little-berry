import vlc
import time


import BaseDados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn)  # faz referência à base de dados das configurações
controldb = BaseDados.LittleBerryControl(conn)  # faz referência à base de dados de controle dos processos

# Class responsável pela parte gráfica do robô, utilizando vídeos guardados no Raspberry Pi
# Esta classe é executada em segundo plano e recebe ordens da class main
# Class com processos sensíveis: não, mas é muito importante
# Proteção contra erros: Sim a todos os niveis, erros são guardados na base de dados
# Nível de Recursos utilizados: imagens-Baixo  videos-Alto ou Muito Alto
class PlayerClass:
  
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()


    def playVideo(self):
        # O objetivo deste método é receber o número do vídeo da classe principal e definir o caminho do vídeo ou imagem para reprodução.
        '''
        1 - piscar 
        2 - bluetooth off
        3 - bluetooth on
        4 - olhos esquerda
        5 - olhos direita
        404 - erro
        '''

        
        try:
            videoAtual = 300 # controla o vídeo atual para otimização
            controldb.CONTROLplayvideo=  1
            url = '/home/daniel/Documents/Faces/ola.mp4'
            media = self.instance.media_new(url)
            self.player.set_media(media)
            self.player.play()
            time.sleep(10)

            while True: 
                time.sleep(0.5)
                nDoVideo = controldb.CONTROLplayvideo
                if videoAtual != nDoVideo:  # verifica se o número do vídeo mudou para evitar reinicializações desnecessárias
                    
                    if nDoVideo == 0:
                        url = '/home/daniel/Documents/Faces/ola.mp4'
                    elif nDoVideo == 1:
                        url = '/home/daniel/Documents/Faces/piscar.mp4'  # caminho para os vídeos
                    elif nDoVideo == 2:
                        url = '/home/daniel/Documents/Faces/bluetooth off.mp4'
                    elif nDoVideo == 3:
                        url = '/home/daniel/Documents/Faces/bluetooth on.mp4'
                    elif nDoVideo == 4:
                        url = '/home/daniel/Documents/Faces/olhos esquerda.mp4'
                    elif nDoVideo == 5:
                        url = '/home/daniel/Documents/Faces/olhos direita.mp4'
                    elif nDoVideo == 6:
                        url = '/home/daniel/Documents/Faces/chamada.mp4'
                    elif nDoVideo == 7:
                        url = '/home/daniel/Documents/Faces/horas.png' 
                    elif nDoVideo == 8:
                        url = '/home/daniel/Documents/Faces/luz.png' 
                    elif nDoVideo == 9:
                        url = '/home/daniel/Documents/Faces/shutdown.png'
                    elif nDoVideo == 10:
                        url = '/home/daniel/Documents/Faces/cronometro.png'  
                    elif nDoVideo == 11:
                        url = '/home/daniel/Documents/Faces/camera.png'
                    elif nDoVideo == 12:
                        url = '/home/daniel/Documents/Faces/timer.png' 
                    elif nDoVideo == 404:
                        url = '/home/daniel/Documents/Faces/erro.mp4'


                
                    else:  
                        # se o número do vídeo não corresponder a um caso específico, assume-se que é um arquivo de imagem com nome correspondente, o formato destes numeros sao **_**
                        url = f'/home/daniel/Documents/Faces/{nDoVideo}.png'
                    
                    media = self.instance.media_new(url)  # cria uma instância de mídia com o caminho especificado


                    

                    
                    self.player.set_media(media)  # define o player com a nova mídia
                    videoAtual = nDoVideo  # atualiza o vídeo atual 
                    self.player.play()  # inicia a reprodução do vídeo ou imagem
                    time.sleep(0.5)  # aguarda para evitar reinicializações rápidas
                    
                else:
                    value = self.player.is_playing() 

                    if value == 0:  # verifica se o vídeo atual terminou para reiniciar (loop)
                        media = self.instance.media_new(url)
                        self.player.set_media(media)
                        videoAtual = nDoVideo
                        self.player.play()
                        time.sleep(0.5)  # aguarda para evitar reinicializações rápidas
        except Exception as e:  # tratamento de erros genérico
            try:  
                # tenta sinalizar um erro visualmente com LEDs vermelhos (se aplicável)
                print("Erro ao reproduzir o vídeo:", e)
                
                value = self.player.is_playing()
                if value == 0:  # se não estiver reproduzindo, tenta exibir um vídeo de erro
                    url = '/home/daniel/Documents/Faces/erro.mp4'
                    self.player.set_media(url)
                    videoAtual = nDoVideo
                    self.player.play()
                    time.sleep(0.5)  # aguarda para evitar reinicializações rápidas
            except Exception as e:  
                # se falhar ao exibir o vídeo de erro, sinaliza um problema fatal na base de dados
                print("Erro fatal ao tentar exibir vídeo de erro:", e)
                controldb.FATALERRORplayVideo = True

        
  
        

if __name__ == "__main__":
    playerTeste = PlayerClass()
    playerTeste.playVideo()
