import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

class RealTimeCurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
    
    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = converter

        # self.configure(background = 'light-gray')
        self.geometry("530x250")

        # Label
        self.intro_label = Label(self, text='Realtime Currency Converter', fg='black', bg='lightblue', relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font=('Helvetica', 15, 'bold'))
        self.intro_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

        self.date_label = Label(self, text=f" Date : {self.currency_converter.data['date']}", relief=tk.GROOVE,
                                borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=200, y=50)