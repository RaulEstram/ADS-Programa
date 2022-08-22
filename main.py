from dotenv import load_dotenv, find_dotenv

from tkinter import *
from interfaces.masterFrame import MasterFrame

load_dotenv(find_dotenv())

# Creamos una ventana
root = Tk()

root.title("Búsqueda de Datos ADS")

app_width = 850
app_height = 500
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w / 2) - (app_width / 2)
y = (screen_h / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Creamos un MasterFrame que tendra todos los widgets de nuestra app
masterFrom = MasterFrame(root)

if __name__ == "__main__":
    masterFrom.mainloop()
