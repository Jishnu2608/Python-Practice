import requests
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def get_joke(label_text):
    url = "https://icanhazdadjoke.com"
    headers = {'Accept': 'application/json'}
    joke_time = requests.get(url, headers=headers).json().get('joke')
    label_text.set(joke_time)
    print(joke_time)
    