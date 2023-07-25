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

        def on_leave1(e):
            but_convert['background'] = "SystemButtonFace"
            but_convert['foreground'] = "SystemButtonText"

        def on_enter2(e):
            but_clear['background'] = "black"
            but_clear['foreground'] = "cyan"

        def on_leave2(e):
            but_clear['background'] = "SystemButtonFace"
            but_clear['foreground'] = "SystemButtonText"

        def clear():
            answer.set("")
            value.set("")
            froms.set("Select Units Convert From")
            to.set("Select Units Convert To")
            real_answer.config(text="")

        def convert():
            try:
                if froms.get() != "Select Units Convert From":
                    if to.get() != "Select Units Convert To":
                        if len(value.get()) != 0:

                            url = 'https://neutrinoapi.net/convert'
                            params = {
                                'user-id': 'Reonnie26',
                                'api-key': '[YOUR_API_KEY]',
                                'from-value': '{}'.format(value.get()),
                                'from-type': '{}'.format(froms.get()),
                                'to-type': '{}'.format(to.get())
                            }

                            postdata = parse.urlencode(params).encode()
                            req = request.Request(url, data=postdata)
                            response = request.urlopen(req)
                            result = json.loads(response.read().decode("utf-8"))
                            name = json.dumps(result, indent=4)
                            real_answer = result['result-float']
