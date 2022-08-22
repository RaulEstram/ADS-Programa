from tkinter import *

from elements.customTextArea import CustomTextArea


class WindowsText(Tk):

    def __init__(self, txt: str, title: str = 'Informacion'):
        super().__init__()
        app_width = 600
        app_height = 350
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w / 2) - (app_width / 2)
        y = (screen_h / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title(title)
        self.frame = Frame(self)
        self.frame.config(bg="pink")
        self.frame.pack(expand=True, fill=BOTH)
        self.area = CustomTextArea(self.frame)
        self.area.setText(txt)
