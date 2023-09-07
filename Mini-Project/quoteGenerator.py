import requests
import ttkbootstrap as ttk

URL = "https://api.quotable.io/random"

def fetch_quote():
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author