import tkinter as tk
from tkinter import *


class CustomTextArea:

    def __init__(self, master):
        self.master = master
        self.scrollX = None
        self.scrollY = None
        self.textArea = None
        self.master.config(bg="#fff")
        self.createTextArea()
        self.responsive()

    def createTextArea(self):
        self.createScrolls()
        self.textArea = Text(self.master, wrap=NONE, xscrollcommand=self.scrollX.set, yscrollcommand=self.scrollY.set)
        self.textArea.config(width=1, height=1)
        self.textArea.grid(column=0, row=0, sticky="nsew")
        self.scrollX.config(command=self.textArea.xview)
        self.scrollY.config(command=self.textArea.yview)
        pass

    def createScrolls(self):
        self.scrollY = Scrollbar(self.master)
        self.scrollY.grid(column=1, row=0, sticky="nsew")

        self.scrollX = Scrollbar(self.master, orient=tk.HORIZONTAL)
        self.scrollX.grid(column=0, row=1, sticky="nsew")

    def responsive(self):
        self.master.rowconfigure(0, weight=1000)
        self.master.columnconfigure(0, weight=1000)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(1, weight=1)

    def setText(self, txt):
        self.textArea.insert(tk.INSERT, txt)

    def getText(self):
        return self.textArea.get("1.0", tk.END)

    def deleteText(self):
        self.textArea.delete("1.0", tk.END)
