import vlc
import time
import signal
import sys

class player:


    
    # Replace with the actual path to your video file
    video_path = '/home/daniel/Downloads/2.mp4'

    # Create a VLC instance
    instance = vlc.Instance()

    # Create a media player
    player = instance.media_player_new()

    # Load the video file
    media = instance.media_new(video_path)
    player.set_media(media)

    # Set full screen mode
    player.set_fullscreen(True)



    # Play the video
    player.play()

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