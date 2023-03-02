import tkinter as tk
from tkinter import *

class CreateWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")
        for r in range(7):
            self.master.rowconfigure(r, weight=1)    
        for c in range(6):
            self.master.columnconfigure(c, weight=1)
        Frame1 = Frame(master, highlightbackground="black", highlightthickness=1)  # Input Fields
        Frame1.grid(row = 0, column = 0, rowspan = 4, columnspan = 3, sticky = W+E+N+S) 
        Frame2 = Frame(master, highlightbackground="black", highlightthickness=1) # Colours Selection
        Frame2.grid(row = 3, column = 0, rowspan = 4, columnspan = 3, sticky = W+E+N+S)
        Frame3 = Frame(master, highlightbackground="black", highlightthickness=1) # Image Input
        Frame3.grid(row = 0, column = 3, rowspan = 4, columnspan = 3, sticky = W+E+N+S)
        Frame4 = Frame(master, highlightbackground="black", highlightthickness=1)# Type Selection
        Frame4.grid(row = 3, column = 3, rowspan = 4, columnspan = 3, sticky = W+E+N+S)
        
        
        

root = Tk()
root.geometry("1280x720")
app = CreateWindow(master=root)
app.mainloop()