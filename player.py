# roomsounds-player
# Joshua Peacocke
# This recieves the information from the Raspberry Pi and takes it be played
# from selecting various songs

from pygame import mixer
# TEMPORARY INPUTS
tags = ['sun', 'afternoon']
song = 'Signs-Of-Love.wav'
mixer.init()
mixer.music.load("music/" + song)
mixer.music.set_volume(1)
mixer.music.play()

while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break