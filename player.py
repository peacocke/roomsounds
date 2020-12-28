# roomsounds-player
# Joshua Peacocke
# This recieves the information from the Raspberry Pi and takes it be played
# from selecting various songs

# import library pygame for playing music and random for playlist shuffling
# math for rounding, and pickle for loading in songs
from math import floor
# Using player from pygame as well as the event functions
import pygame
# Shuffling playlists
import random
# getting local time
import time
# to load prepared songs
import pickle

print("Song addition, files must be in .ogg format to play")
# Creates a class for songs with their attached tags
class Song:
    def __init__(self, name, tag):
        # Assign the tags and song name
        self.tags = tag
        self.name = name


# The main player
class Player:
    def __init__(self):
        # Create an event when music ends
        self.MUSIC_END = pygame.USEREVENT + 1
        # Set variable current song to none
        self.current_song = None
        # Start up pygame and the mixer
        pygame.init()
        pygame.mixer.music.set_volume(1)

    def load_music(self):
        # Create the list of songs to be chosen from
        playlist = decide_playlist()
        # as long as more than one song is in play
        if len(playlist) > 1:
            # Ensure that the next coming song is not the same as the current
            song = self.current_song
            # Until a differnent song is chosen, keep choosing
            while self.current_song == song:
                song = random.choice(playlist)
        else:
            # Otherwise next song is the same
            song = playlist[0]
        # Change to a new current song
        self.current_song = song
        # Create an event when music ends
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        # Put in the new song to be played
        print(song)
        pygame.mixer.music.load('music/' + song)
        pygame.mixer.music.play()
        print("CURRENTLY PLAYING " + self.current_song)
        self.running()

# while the player is running, detect when music stopped
    def running(self):
        while True:
            for event in pygame.event.get():
                # Load the next song once MUSIC END event is triggered
                if event.type == self.MUSIC_END:
                    print("Music ended")
                    self.load_music()


# TEMPORARY INPUTS



# How a playlist is made based on tags
def decide_playlist():
    playlist = []
    tag_list = tag_define()
    # For each song in the list
    for song in total_songs:
        # If all the tags made are in the tags for a song, add to the list
        if all(tags in song.tags for tags in tag_list):
            print('added' + song.name)
            playlist.append(song.name)
    print(playlist)
    return playlist


def tag_define():
    new_tags = []
    # Time tag
    # Find current local hour, split into 3 hour chunks
    # 0000 to 0300 = 0, 0300 to 0600 = 1, 0600 to 0900 = 2
    # 0900 to 1200 = 3, 1200 to 1500 = 4, 1500 to 1800 = 5
    # 1800 to 2100 = 6, 2100 to 2400 = 7
    current_hour = floor(time.localtime().tm_hour / 3)
    time_tag = {0: 'late night',
                1: 'late night',
                2: 'early morning',
                3: 'morning',
                4: 'lunchtime',
                5: 'afternoon',
                6: 'night',
                7: 'late night'}[current_hour]
    new_tags.append(time_tag)
    weather_tag = input("Is it raining or sunny?")
    new_tags.append(weather_tag)
    print(new_tags)
    return new_tags

if __name__ == "__main__":
    song_file = open('song_pickle','rb')
    total_songs = pickle.load(song_file)
    for song in total_songs: print(song.name)
    roomsounds = Player()
    roomsounds.load_music()
