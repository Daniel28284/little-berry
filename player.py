import vlc
import time
import signal
import sys

class player1:
    #video_path = '/home/daniel/Downloads/2.mp4'
    caraFeliz=0#'caminho para o video'
    caraTriste=0#'caminho pra o o video'


    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()


    def playVideo(self,nDoVideo=1):
         #video_path = '/home/daniel/Documents/little-berry/Faces/'
        '''
        1-sad
        2-happy

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

        event_manager = self.player.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.on_end_reached)
       

        self.player.play()

        time.sleep(3)


        

        while True:
            pass


    def teste(self):
        media = self.instance.media_new('/home/daniel/Documents/little-berry/Faces/piscar.mp4')
        self.player.set_media(media)
        
    

    

    def on_end_reached(self, event):
        print("O vídeo terminou de ser reproduzido.")
        self.player.stop()
        

        



if __name__ == "__main__":
    print("eu sou um teste de imagem ")
    playerTeste=player1()
    playerTeste.playVideo()
   