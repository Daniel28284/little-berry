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


    def playVideo(self):
        '''
        1-sad
        2-happy

        '''
        #video_path = '/home/daniel/Documents/little-berry/Faces/'
        caraPiscar='/home/daniel/Documents/little-berry/Faces/bluetooth off.mp4'
        caraTriste=0#'caminho pra o o video'

        
        
        media = self.instance.media_new(caraPiscar)
        self.player.set_media(media)

       

        
        
        # Play the video
        self.player.play()

        while True:
            pass


    def all(self):
        print("ola")

        



if __name__ == "__main__":
    print("eu sou um teste de imagem ")
    playerTeste=player1()
    playerTeste.playVideo()
   