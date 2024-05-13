import vlc
import time
import signal
import sys

class playerClass:
    #video_path = '/home/daniel/Downloads/2.mp4'
    caraFeliz=0#'caminho para o video'
    caraTriste=0#'caminho pra o o video'


    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()


    def playVideo(self,nDoVideo=1):
         #video_path = '/home/daniel/Documents/little-berry/Faces/'
        '''
        1-piscar 
        2-bluetooth off
        3-bluetooth on
        4-olhos esquerda
        5-olhos direita
        404-erro
        '''

        if(nDoVideo==1):
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
        
        
        media = self.instance.media_new(url)
        self.player.set_media(media)

        
       

        self.player.play()

        time.sleep(3)


        

        while True:
            pass


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
    print("eu sou um teste de imagem ")
    playerTeste=playerClass()
    playerTeste.teste()
    print("teste de imagem completo")
    playerTeste.playVideo()
   