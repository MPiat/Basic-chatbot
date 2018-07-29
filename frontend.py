# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:01:04 2018

@author: Michal Piatek
"""

import tkinter as tk
from tkinter import ttk
import chatbot_backend as cb


win = tk.Tk()
win.title("Chatbot")
win.resizable(0, 0)
response = ttk.Label(win, text = "")
response.grid(column=0,row=0, columnspan=3)

def clickMe(self):
    response.configure(text=cb.get_response(question.get()))
    
question = tk.StringVar()
questionEntered = ttk.Entry(win, width=32, textvariable = question)
questionEntered.focus()
questionEntered.grid(column=1,row=1)
action = ttk.Button(win, text = "Enter", command = clickMe)
win.bind('<Return>', clickMe)
action.grid(column=1, row=2)

win.mainloop()
