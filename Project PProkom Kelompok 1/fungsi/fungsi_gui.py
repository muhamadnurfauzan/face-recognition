import tkinter as tk
from tkinter import filedialog
import shutil
import os

def foto() :
    foto = tk.filedialog.askopenfilename()
    shutil.move(foto, "student")

def hapus() :
    foto = tk.filedialog.askopenfilename()
    os.remove(foto)
