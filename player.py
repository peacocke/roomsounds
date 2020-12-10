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
        pygame.mixer.music.set_volume(1)

    def decide_playlist(self):
        for playlist in total_songs:
            if (tags[0] in playlist.tags) and (tags[1] in playlist.tags):
                return playlist

    def load_music(self):
        playlist = self.decide_playlist()
        song = self.current_song
        while self.current_song == song:
            song = random.choice(playlist.songs)
        self.current_song = song
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        pygame.mixer.music.load('music/' + song)
        pygame.mixer.music.play()
        print("CURRENTLY PLAYING " + self.current_song)
        self.running()

    def running(self):
        while True:
            print("p for pause, r for resume, e for exit")
            print("t to change tags")
            query = input("")
            if query == 'p':
                pygame.mixer.music.pause()
                print("PAUSED")
            elif query == 'r':
                pygame.mixer.music.unpause()
                print("RESUMED")
            elif query == 'e':
                pygame.mixer.music.stop()
                print("EXITING...")
                break
            elif query == 't':
                change_tags()
            for event in pygame.event.get():
                if event.type == self.MUSIC_END:
                    print("Music ended")
                    self.load_music()


            

# TEMPORARY INPUTS


total_songs = [Playlist(['sun', 'afternoon'], ['Signs-Of-Love.wav']),
               Playlist(['rain', 'afternoon'], ['Beneath-The-Mask.wav']),
               Playlist(['sun', 'rain', 'night'], ['Iwatodai-Station.wav'])]
tags = ['rain', 'night']


def change_tags():
    global tags
    tags = [input("enter first tag"), input("input second tag")]


roomsounds = Player()
roomsounds.load_music()
