from tkinter import Entry, Label, Checkbutton, mainloop, Button
from logic import Logic


class Interface(Logic):
    def __init__(self):
        super().__init__()
    
    def mainInterface(self):
        Entry(self.root, textvariable = self.linkEntry, width = 25, bg="light blue").place(x= 140, y = 150)
        Label(self.root, text = "YT Link", fg = "black",font = ("Segoe UI", 9)).place(x= 90, y = 148)
        Checkbutton(self.root, text = "Save as mp3", variable = self.saveAsMp3).place(x = 260, y = 148)
        Button(self.root, text = "Download", bg = "black", fg = "white",font =("Segoe UI", 7), command = lambda *args: self.downloadVideo()).place(x = 168, y = 260)

        self.root.mainloop()

if __name__ == "__main__":
    Interface().mainInterface()

