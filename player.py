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

         #video_path = '/home/daniel/Documents/Faces/'
       
        


        
        


        try:
            videoAtual=300
            while True:

                nDoVideo=controldb.CONTROLplayvideo
                if videoAtual!=nDoVideo:

                    if nDoVideo==0:
                        url=0 #meter o url de um video de carregamento
                    elif nDoVideo==1:
                         url='/home/daniel/Documents/Faces/piscar.mp4'
                    elif nDoVideo==2:
                         url='/home/daniel/Documents/Faces/bluetooth off.mp4'
                    elif nDoVideo==3:
                         url='/home/daniel/Documents/Faces/bluetooth on.mp4'
                    elif nDoVideo==4:
                         url='/home/daniel/Documents/Faces/olhos esquerda.mp4'
                    elif nDoVideo==5:
                         url='/home/daniel/Documents/Faces/olhos direita.mp4'
                    elif nDoVideo==404:
                        url='/home/daniel/Documents/Faces/erro.mp4'
                        

                    else:
                        url = f'/home/daniel/Documents/Faces/{nDoVideo}.png'
                    
                    media = self.instance.media_new(url)
                    self.player.set_media(media)
                    videoAtual=nDoVideo
                    self.player.play()
                    time.sleep(1)
                    
                else:
                    value = self.player.is_playing()

                    if value == 0:

                        media = self.instance.media_new(url)
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
                    url='/home/daniel/Documents/Faces/erro.mp4'
                    self.player.set_media(url)
                    videoAtual=nDoVideo
                    self.player.play()
                    time.sleep(1) #delay para dar tempo de iniciar o video
            except:
                controldb.FATALERRORplayVideo=True


            


    def teste(self):
        try:
            videoAtual=300
            nDoVideo=controldb.CONTROLplayvideo
            if videoAtual!=nDoVideo:
                print(nDoVideo)


            

            media = self.instance.media_new('/home/daniel/Documents/Faces/piscar.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(3)
            

            media = self.instance.media_new('/home/daniel/Documents/Faces/bluetooth off.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(10)


            media = self.instance.media_new('/home/daniel/Documents/Faces/bluetooth on.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(10)

            media = self.instance.media_new('/home/daniel/Documents/Faces/olhos esquerda.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(15)


            media = self.instance.media_new('/home/daniel/Documents/Faces/olhos direita.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(15)


            media = self.instance.media_new('/home/daniel/Documents/Faces/erro.mp4')
            self.player.set_media(media)
            self.player.play()
            time.sleep(3)
        
        except:
            print("ola")

    
        

        

        

        

        
    

    

  
        

        



if __name__ == "__main__":

    print("eu sopu um teste de imagem ")
    playerTeste=PlayerClass()
    #playerTeste.teste()
    print("teste de imagem completo")
    playerTeste.playVideo()
    
   