import tkinter as tk


class CustomEntry(tk.Entry):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.config(
            bg="#fff",
            font=("Arial", 10),
            relief=tk.SOLID,
            borderwidth=1,
            highlightcolor="#156789",
            justify=tk.LEFT,
            selectbackground="#1a1a1a",
            selectborderwidth=0,
            selectforeground="#fff",
        )
