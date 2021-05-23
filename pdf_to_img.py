import fitz
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import easygui
from os import path
import os


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PDF To Image")
        self.window.geometry("500x400")
        self.window.configure(bg="#1E2127")
        try:
            os.mkdir("Images")
        except:
            pass

        w = tk.Button(
            self.window,
            activebackground="#E44A53",
            bg="#161719",
            fg="#FFFFFF",
            text="Upload File",
            command=self.checker,
            height=3,
            width=8,
        ).place(x=40, y=40)
        self.window.mainloop()

    def checker(self):
        self.window.destroy()
        self.filepath = easygui.fileopenbox()
        print(self.filepath)
        self.waiting_window()

    def waiting_window(self):
        self.window = tk.Tk()
        self.window.title("PDF To Image")
        self.window.geometry("500x400")
        self.window.configure(bg="#1E2127")

        L = tk.Label(
            self.window,
            text="Please wait, Creating Images from PDF.",
            bg="#161719",
            fg="#FFFFFF",
            font=("Arial", 18),
        ).place(x=40, y=40)
        self.image_scrape_save()
        self.window.mainloop()

    def image_scrape_save(self):
        file = fitz.open(self.filepath)
        for pagnNumber, page in enumerate(file.pages(), start=1):
            text = page.getText()
            names = text.split("\n")
            for imgNumber, img in enumerate(page.getImageList(), start=1):
                xref = img[0]
                pix = fitz.Pixmap(file, xref)
                if pix.n > 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                pix.writePNG(f"Images/{names[imgNumber-1]}.png")
        self.window.destroy()


obj = Main()