import os
import sys
import json
import time
import logging
import datetime
import subprocess
import configparser

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from PIL import Image, ImageTk
import customtkinter 
from datetime import date
from tkcalendar import *

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
ChildWindow = None
        
root = customtkinter.CTk()
root.geometry("1280x720")
root.title("Admin Application")

global_font = customtkinter.CTkFont(family="MS Sans Serif", size=32)

for r in range(7):
    root.grid_rowconfigure(r, weight=1)    
for c in range(6):
    root.grid_columnconfigure(c, weight=1)
    
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1)
    
InputFieldFrame = customtkinter.CTkFrame(master=root, height=340, width=620)
ColourSelectFrame = customtkinter.CTkScrollableFrame(root, height=328, width=602)
ImageInputFrame = customtkinter.CTkFrame(root, height=340, width=620)
TypeSelectionFrame= customtkinter.CTkScrollableFrame(root, height=328, width=602)

##### Input Field Frame #####
DateSelection = StringVar(value=date.today())
ChildFont = customtkinter.CTkFont(family="MS Sans Serif", size=16)

def CloseWindow():
    global ChildWindow
    ChildWindow.destroy()

def SubmitDate(Date):
    global DateSelection
    DateSelection.set(Date)
    DateInput.configure(text= DateSelection.get())
    CloseWindow()
    
def OpenWindow():
    global ChildWindow
    if ChildWindow is None or not ChildWindow.winfo_exists():
        
        ChildWindow = customtkinter.CTkToplevel(root)
        ChildWindow.geometry("400x300")
        ChildWindow.title("Select Date")
        
        ChildFrame = customtkinter.CTkFrame(ChildWindow)
        
        Label = customtkinter.CTkLabel(ChildFrame, text="Date Found", font=global_font)
        Label.grid(row=0, column=0)
        
        DateSelector = Calendar(ChildFrame, selectmode='day', maxdate=date.today(), font=ChildFont, date_pattern="yyyy-mm-dd")
        DateSelector.grid(row = 1, column=0)
        
        OkayButton = customtkinter.CTkButton(ChildFrame, width=60, height=16, text="Confirm", font=ChildFont, hover_color="white", command=lambda:SubmitDate(DateSelector.get_date()))
        CancelButton = customtkinter.CTkButton(ChildFrame, width=60, height=16, text="Cancel", font=ChildFont, fg_color="red", hover_color="white", command=CloseWindow)
        
        OkayButton.grid(row = 2, column = 0)
        CancelButton.grid(row = 2, column = 1)
        
        ChildFrame.pack(padx=15, pady=15)
        ChildWindow.grab_set()
    else:
        ChildWindow.focus()

ItemNameLabel = customtkinter.CTkLabel(InputFieldFrame, text="Item Name:", font=global_font, justify="left")
ItemNameLabel.grid(row=1, column=1, padx=(15, 0), pady=10)
ItemNameInput = customtkinter.CTkEntry(InputFieldFrame, font=global_font, width=300)
ItemNameInput.grid(row=1, column=2, padx=(0, 10), pady=10)

LocationLabel = customtkinter.CTkLabel(InputFieldFrame, text=" Location Found: ", font=global_font, justify="left")
LocationLabel.grid(row=2, column=1, padx=(15, 0), pady=10)
LocationInput = customtkinter.CTkEntry(InputFieldFrame, font=global_font, width=300)
LocationInput.grid(row=2, column=2, padx=(0, 10), pady=10)

DateLabel = customtkinter.CTkLabel(InputFieldFrame, text="Date Found:", font=global_font)
DateLabel.grid(row=3, column=1, padx=(15, 0), pady=10)
DateInput = customtkinter.CTkButton(InputFieldFrame, text=DateSelection.get(), font=global_font, command=OpenWindow, width=300)
DateInput.grid(row=3, column=2, padx=(0, 10), pady=10)

InputFieldFrame.grid_columnconfigure(0, weight=1)
InputFieldFrame.grid_columnconfigure(3, weight=1)
InputFieldFrame.grid_rowconfigure(0, weight=1)
InputFieldFrame.grid_rowconfigure(4, weight=1)

##### Image Input Frame #####




InputFieldFrame.grid(row=0, column=0)
ColourSelectFrame.grid(row=1, column=0)
ImageInputFrame.grid(row=0, column=1)
TypeSelectionFrame.grid(row=1, column=1)

InputFieldFrame.grid_propagate(False)

root.mainloop()
