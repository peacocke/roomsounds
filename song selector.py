from tkinter import filedialog
import tkinter as tk
import pickle as pkl
from player import Song
import glob, os
try:
    song_file = open('song_pickle', 'rb')
    song_list = pkl.load(song_file)
    song_file.close()
except (EOFError, FileNotFoundError):
    song_list = []
root = tk.Tk


def add_songs():
    song_file = open('song_pickle','wb')
    root.directory = filedialog.askdirectory()
    print(root.directory)
    os.chdir(root.directory)
    for file in glob.glob("*.ogg"):
        print(file)
        tags = []
        while True:
            new_tag = input("Add an extra tag, exit by entering 'X'")
            if new_tag != 'X':
                tags.append(new_tag)
            else:
                break
        further = input("add more songs?")
        if further == 'n':
            break
        song_list.append(Song(file, tags))
    pkl.dump(song_list, song_file)
    song_file.close()


add_songs()
