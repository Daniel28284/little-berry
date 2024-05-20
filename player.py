import vlc
import time
import signal
import sys

import BaseDados



conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)



class PlayerClass:
    #video_path = '/home/daniel/Downloads/2.mp4'
    caraFeliz=0#'caminho para o video'
    caraTriste=0#'caminho pra o o video'


    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()


    def playVideo(self):
        '''
        1-piscar 
        2-bluetooth off
        3-bluetooth on
        4-olhos esquerda
        5-olhos direita
        404-erro
        '''

         #video_path = '/home/daniel/Documents/little-berry/Faces/'
       
        url='/home/daniel/Documents/little-berry/Faces/erro.mp4'


        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.play()

        time.sleep(5)


        
        


        try:
            while True:

                nDoVideo=controldb.CONTROLplayvideo
                if videoAtual!=nDoVideo:

                    if nDoVideo==0:
                        url=0 #meter o url de um video de carregamento
                    elif(nDoVideo==1):
                        url='/home/daniel/Documents/little-berry/Faces/piscar.mp4'
                    elif(nDoVideo==2):
                        url='/home/daniel/Documents/little-berry/Faces/bluetooth off.mp4'
                    elif(nDoVideo==3):
                        url='/home/daniel/Documents/little-berry/Faces/bluetooth on.mp4'
                    elif(nDoVideo==4):
                        url='/home/daniel/Documents/little-berry/Faces/olhos esquerda.mp4'
                    elif(nDoVideo==5):
                        url='/home/daniel/Documents/little-berry/Faces/olhos direita.mp4'
                    elif(nDoVideo==404):
                        url='/home/daniel/Documents/little-berry/Faces/erro.mp4'
                else:
                    value = self.player.is_playing()
                    if value == 0:
                        self.player.set_media(media)
                        videoAtual=nDoVideo
                        self.player.play()
                        time.sleep(1) #delay para dar tempo de iniciar o video
        except:
            try:
                print("erro a representar o video")
                controldb.ERRORplayVideo=True
                value = self.player.is_playing()
                if value == 0:
                    url='/home/daniel/Documents/little-berry/Faces/erro.mp4'
                    self.player.set_media(media)
                    videoAtual=nDoVideo
                    self.player.play()
                    time.sleep(1) #delay para dar tempo de iniciar o video
            except:
                controldb.FATALERRORplayVideo=True


            


    def teste(self):
        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/piscar.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(3)
        

        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/bluetooth off.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(10)


        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/bluetooth on.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(10)

        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/olhos esquerda.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(15)


        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/olhos direita.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(15)


        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/erro.mp4')
        self.player.set_media(media)
        self.player.play()
        time.sleep(3)
        


    
        

        

        

        

        
    

    

  
        

        



if __name__ == "__main__":

    print("eu sopu um teste de imagem ")
    playerTeste=PlayerClass()
    playerTeste.teste()
    print("teste de imagem completo")
    #playerTeste.playVideo()
    
   