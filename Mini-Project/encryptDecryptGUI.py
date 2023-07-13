import tkinter as tk
import tkinter.font as tkfont
from tkinter import *

#Create a tkinter root window
root = tk.Tk()

root.title("Text Encryptor-Decryptor")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

#Create a canvas to add widgets
canvas = tk.Canvas(root,height = 500, width=400, bg="LightBlue")
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")
