import tkinter as tk
from tkinter import *

from elements.customEntry import CustomEntry
from elements.customLabel import CustomLabel
from elements.customButton import CustomButton


class EntryMessage(Tk):

    def __init__(self, txt: str, title: str = 'Informacion', command=print, arg=None):
        super().__init__()
        app_width = 250
        app_height = 120
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w / 2) - (app_width / 2)
        y = (screen_h / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title(title)
        self.resizable(False, False)

        self.frame = None
        self.entry = None
        self.label = None
        self.acceptButton = None
        self.cancelButton = None

        self.text = None
        self.command = command
        self.arg = arg

        self.initialize(txt)
        self.responsive()

    def initialize(self, txt: str):
        # Creamos un frame donde estaran nuestros widgets
        self.frame = Frame(self)
        self.frame.config(bg="#fff")
        self.frame.pack(expand=True, fill=tk.BOTH)
        # Creamos un Label
        self.label = CustomLabel(self.frame, txt)
        self.label.config(anchor=tk.CENTER)
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        # Creamos un Entry
        self.entry = CustomEntry(self.frame)
        self.entry.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        # Creando los botones
        self.acceptButton = CustomButton(self.frame, "Aceptar", command=lambda: self.ok(self.entry.get()))
        self.acceptButton.grid(row=3, column=0, sticky="nsew", pady=5, padx=20)

        self.cancelButton = CustomButton(self.frame, "Cancelar", command=self.cancel)
        self.cancelButton.grid(row=3, column=1, sticky="nsew", pady=5, padx=20)

    def responsive(self):
        rows = 4
        columns = 2
        for i in range(rows):
            self.frame.rowconfigure(i, weight=1)
        for i in range(columns):
            self.frame.columnconfigure(i, weight=1)
        self.frame.rowconfigure(1, weight=4)

    def ok(self, txt: str):
        self.command(txt, self.arg)
        self.destroy()

    def cancel(self):
        self.destroy()
