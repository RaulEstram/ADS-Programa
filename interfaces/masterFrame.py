import tkinter as tk
from tkinter import Frame, Label

from interfaces.menu import BarMenu
from interfaces.home import Home


class MasterFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.barMenu = None
        self.title = None
        self._focusWidget = None
        self.titleFrame = None
        self.config(
            bg="#fff",
            relief=tk.FLAT,
            width=700,
            height=450
        )
        self.pack(expand=True, fill=tk.BOTH)
        self.createBarMenu()
        self.createTitle()
        self.loadHome()

    def loadHome(self):
        home = Home(self)
        home.place(relx=0.2, rely=0.15, relwidth=0.8, relheight=0.85)
        self._focusWidget = home

    def createBarMenu(self):
        self.barMenu = BarMenu(self, self.createFrame)
        self.barMenu.place(x=0, y=0, relwidth=0.2, relheight=1)

    def createTitle(self):
        self.titleFrame = Frame(self)
        self.titleFrame.config(bg="#1a1a1a")
        self.titleFrame.place(relx=0.2, y=0, relwidth=0.8, relheight=0.15)
        self.title = Label(self.titleFrame)
        self.title.config(text="Menu", fg="#bfbfbf", bg='#1a1a1a', font=("JetBrains Mono", 25))
        self.title.pack(fill=tk.BOTH, expand=True)

    def createFrame(self, widget, title):
        if self._focusWidget is not None:
            self.deleteFrame()
        self._focusWidget = widget(self)
        self._focusWidget.place(relx=0.2, rely=0.15, relwidth=0.8, relheight=0.85)
        self.title.config(text=title)

    def deleteFrame(self):
        self._focusWidget.destroy()
