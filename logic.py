from pytube import YouTube
from os import curdir, remove, close
from tkinter import Tk, StringVar, BooleanVar, mainloop


class Logic():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x300")
        self.root.title("musicManager")
        self.saveAsMp3 = BooleanVar()
        self.linkEntry = StringVar()
    
    def downloadVideo(self):
        saveStatus = self.saveAsMp3.get()
        youtubeLink = self.linkEntry.get()
        initializeYoutube = YouTube(youtubeLink)
        videoTitle = initializeYoutube.title
        getDownloadObject = initializeYoutube.streams.first()
        getDownloadObject.download(curdir)
    
        if saveStatus:
            import moviepy.editor as movie
            video = movie.VideoFileClip(rf"{curdir}\{videoTitle}.mp4")
            video.audio.write_audiofile(rf"{curdir}\{videoTitle}.mp3")




