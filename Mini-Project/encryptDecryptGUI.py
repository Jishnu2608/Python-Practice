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

#Create a label widget for user instructions
label1 = tk.Label(root,text= "Enter the Text",width=20,bg="LightBlue")
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)

#Create an entry widget for user input
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)

#Create a label for selecting the operation
label2=tk.Label(root,text="Choose an Operation",width=25,bg="LightBlue")
label2.config(font=bold_font)
canvas.create_window(200,200,window=label2)

#tkinter IntVar to store selected operation choice
v = tk.IntVar()

#Function to handle the choice of encryption or decryption
def choice():
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()
