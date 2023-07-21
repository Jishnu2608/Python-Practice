from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from urllib import request, parse
import json

class Units:
    def __init__(self, root):
        self.root = root
        self.root.title("Units Conversion")
        self.root.geometry("500x400")
        self.root.resizable(0, 0)

        froms = StringVar()
        to = StringVar()
        value = StringVar()
        answer = StringVar()

        def on_enter1(e):
            but_convert['background'] = "black"
            but_convert['foreground'] = "cyan"
