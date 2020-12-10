# roomsounds-player
# Joshua Peacocke
# This recieves the information from the Raspberry Pi and takes it be played
# from selecting various songs
import pygame
import random
# TEMPORARY INPUTS


class Playlist:
    def __init__(self, tags, songs):
        self.tags = tags
        self.songs = songs


class Player:
    def __init__(self):
        self.MUSIC_END = pygame.USEREVENT + 1
        self.current_song = None
        pygame.init()
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        pygame.mixer.music.set_volume(1)

    def decide_playlist(self):
        for playlist in total_songs:
            if (tags[0] in playlist.tags) and (tags[1] in playlist.tags):
                return playlist

    def load_music(self, current_song):
        playlist = self.decide_playlist()
        song = None
        while self.current_song == song:
            song = random.choice(playlist.songs)
        current_song = song
        print('playing ' + song)
        pygame.mixer.music.load('music/' + song)
        pygame.mixer.music.play()
    def running(self):
        while True:
            

# TEMPORARY INPUTS


total_songs = [Playlist(['sun', 'afternoon'], ['Signs-Of-Love.wav']),
               Playlist(['rain', 'afternoon'], ['Beneath-The-Mask.wav']),
               Playlist(['sun', 'rain', 'night'], ['Iwatodai-Station.wav'])]
tags = ['rain', 'night']
roomsounds = Player()
roomsounds.load_music(tags)
