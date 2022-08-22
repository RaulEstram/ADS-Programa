from tkinter import Label
import tkinter as tk


class Home(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.config(
            bg="#fff"
        )
        self.loadWidgets()

    def loadWidgets(self):
        titulo = Label(self)
        titulo.config(text="Programa ADS", bg="#fff", font=("JetBrains Mono", 25))
        titulo.grid(row=0, column=0, sticky="nsew", pady=20)
        self.columnconfigure(0, weight=1)
