import vlc
import time
import signal
import sys

class player:
    #video_path = '/home/daniel/Downloads/2.mp4'
    caraFeliz=0#'caminho para o video'
    caraTriste=0#'caminho pra o o video'


    def __init__(self):
        self.instance = vlc.Instance()
        self.player = instance.media_player_new()


    def playVideo(seld, nDoVideo):
        '''
        1-sad
        2-happy

        '''
        #video_path = '/home/daniel/Downloads/2.mp4'
        caraFeliz=0#'caminho para o video'
        caraTriste=0#'caminho pra o o video'

        match nDoVideo:
            case 1:
                media = self.instance.media_new(caraFeliz)
            case 2:
                media = self.instance.media_new(caraTriste)
        
        
        self.player.set_media(media)

        # Set full screen mode
        self.player.set_fullscreen(True)
        # Play the video
        self.player.play()

        try:
            # Wait for 20 seconds
            time.sleep(20)

            # Stop the player to release resources
            player.stop()

            # Replace with the path to the new video file
            new_video_path = '/path/to/your/new/video.mp4'
            new_media = instance.media_new(new_video_path)
            player.set_media(new_media)

            # Play the new video
            player.play()

            # Wait for the new video to finish (you can add more logic here if needed)
            while True:
                pass

        except KeyboardInterrupt:
            # Handle Ctrl+C: Stop the player and exit gracefully
            player.stop()
            sys.exit(0)