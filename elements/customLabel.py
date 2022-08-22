import tkinter as tk


class CustomLabel(tk.Label):

    def __init__(self, master, txt):
        super().__init__(master, text=txt)
        self._master = master
        self.config(
            bg="#fff",
            font=("Arial", 12),
        )
