# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:01:04 2018

@author: Michal Piatek
"""
import tkinter as tk
from tkinter import ttk
import chatbot_backend as cb
from tkinter import Menu


## Creating the main window
win = tk.Tk()
win.title("Chatbot")
win.resizable(0, 0)
response = ttk.Label(win, text = "")
response.grid(column=0,row=0, columnspan=3)

## Functions for the GUI

# Action for asking the question
def _questionAction():
    response.configure(text=cb.get_response(question.get()))
    questionEntered.focus()
    questionEntered.delete(0,1024)
    
# Action for asking the question using enter key.
def _questionActionEnterKey(self):
    _questionAction()
    
# Action for exiting the program    
def _quit():
    win.quit()
    win.destroy()
    exit()
    
# Opening the relearn option window.
def _relearnWindow():
    learnWindow = tk.Tk()
    learnWindow.title("Relearn")
    learnWindow.resizable(0, 0)
    
    label = ttk.Label(learnWindow, text = "Enter the number of pages for bot to learn from - the more the better.")
    label.grid(column=1, row=1)
    
    pagesNumberEntered = ttk.Entry(learnWindow, width=16, textvariable = pagesNumber)
    pagesNumberEntered.grid(column = 1, row = 2)
    pagesNumberEntered.focus()

    action2 = ttk.Button(learnWindow, text = "Relearn", command = lambda: _relearnAction(pagesNumberEntered.get()))
    action2.grid(column=1, row=3)
    
# Action for relearning
def _relearnAction(number):
    cb.ds.scrape(int(number))
    cb.vec, cb.convo_frame = cb.fitting()
    
## Variables declaration
    
# Number of pages to scrape during relearning.
pagesNumber = tk.IntVar()

# Question from the user.
question = tk.StringVar()

## Widgets for the main window.
questionEntered = ttk.Entry(win, width=32, textvariable = question)
questionEntered.focus()
questionEntered.grid(column=1,row=1)
action = ttk.Button(win, text = "Enter", command = _questionAction)
action.grid(column=1, row=2)
# Binding functionality of a button to enter key
win.bind('<Return>', _questionActionEnterKey)

# Creating a menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Creating a Bot learning menu option.
botMenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label="Bot Menu", menu=botMenu)

# Adding a relearn menu item under Bot learning option
botMenu.add_command(label="Relearn", command = _relearnWindow)
botMenu.add_command(label="Exit", command=_quit) 

# Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

## Window loop
win.mainloop()
