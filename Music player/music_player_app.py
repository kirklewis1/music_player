import tkinter as tk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        # create a label to display the current song
        self.song_label = tk.Label(root, text="No song playing", width=50)
        self.song_label.pack()
        # create a play/pause button
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()
        # create a stop button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()
        # create a selector for the songs
        self.song_selector = tk.Spinbox(root, values=("song1.mp3", "song2.mp3", "song3.mp3"))
        self.song_selector.pack()
        # initialize the pygame mixer
        pygame.mixer.init()

    def play_music(self):
        # get the selected song
        song = self.song_selector.get()
        # load the song
        pygame.mixer.music.load(song)
        # update the label
        self.song_label.config(text=f"Playing {song}")
        # start playing the song
        pygame.mixer.music.play()
        # change the button text
        self.play_button.config(text="Pause", command=self.pause_music)

    def stop_music(self):
        # stop the music
        pygame.mixer.music.stop()
        # update the label
        self.song_label.config(text="No song playing")
        # change the button text
        self.play_button.config(text="Play", command=self.play_music)

    def pause_music(self):
        # pause the music
        pygame.mixer.music.pause()
        # update the label
        self.song_label.config(text=f"Paused {self.song_selector.get()}")
        # change the button text
        self.play_button.config(text="Resume", command=self.unpause_music)

    def unpause_music(self):
        # unpause the music
        pygame.mixer.music.unpause()
        # update the label
        self.song_label.config(text=f"Playing {self.song_selector.get()}")
        # change the button text
        self.play_button.config(text="Pause", command=self.pause_music)

# create the GUI
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()




