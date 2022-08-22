import tkinter as tk


class CustomButton(tk.Button):

    def __init__(self, master, txt, command):
        super().__init__(master, command=command)
        self._master = master
        self.config(
            text=txt,
            bg="#354259",
            relief=tk.FLAT,
            bd=0,
            cursor="hand1",
            activebackground="#1a1a1a",
            activeforeground="#C4C4C4",
            foreground="#fff",
            font=("Arial", 12)
        )
