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