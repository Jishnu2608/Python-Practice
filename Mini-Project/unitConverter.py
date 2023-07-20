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
