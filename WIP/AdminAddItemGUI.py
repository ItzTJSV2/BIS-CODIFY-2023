import os
from tkinter import filedialog
import tkinter as tk
from tkinter import *
import shutil
from tkcalendar import *
from PIL import Image
import customtkinter 
from datetime import date
from tkcalendar import *
from addnSearch import addItem
from Database_Calls.UpdateFound import CheckTime

CheckTime()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
ChildWindow = None
filedir = ""
        
root = customtkinter.CTk()
root.resizable(width=False, height=False)
root.geometry("1280x720")
root.title("Admin Application")

global_font = customtkinter.CTkFont(family="MS Sans Serif", size=24)

for r in range(7):
    root.grid_rowconfigure(r, weight=1)    
for c in range(6):
    root.grid_columnconfigure(c, weight=1)
    
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1)
    
InputFieldFrame = customtkinter.CTkFrame(master=root, height=360, width=620)
ColourSelectFrame = customtkinter.CTkScrollableFrame(root, height=308, width=602)
ImageInputFrame = customtkinter.CTkFrame(root, height=360, width=620)
TypeSelectionFrame= customtkinter.CTkScrollableFrame(root, height=308, width=602)

##### Input Field Frame #####
DateSelection = StringVar(value=date.today())
ChildFont = customtkinter.CTkFont(family="MS Sans Serif", size=16)

def Submit():
    if ItemNameInput.get():
        ItemNameLabel.configure(text_color="white")
        if LocationInput.get():
            LocationLabel.configure(text_color="white")
            if filedir != "":
                UploadButton.configure(fg_color="orange", hover_color="dark orange")
                ColourArray = []
                for i in range(len(ColourDict)):
                    if ColourDict[i].get() == 1:
                        ColourArray.append(i)
                addItem(ItemNameInput.get(), LocationInput.get(), f"Images\{os.path.basename(filedir)}", DateSelection.get(), ColourArray, TypeSelection.get(), SecurityChoice.get())
                Reset()
            else:
                UploadButton.configure(fg_color="red", hover_color="dark red")
        else:
            LocationLabel.configure(text_color="red")
    else:
        ItemNameLabel.configure(text_color="red")
def Reset():
    ItemNameInput.delete(0, END)
    LocationInput.delete(0, END)
    filedir=""
    ImageLabel.configure(image="")
    DateSelection.set(date.today())
    DateInput.configure(text= DateSelection.get())
    for i in range(len(ColourDict)):
        ColourDict[i].set(0)
    TypeSelection.set("Misc")
    SecurityChoice.set("Low")
    UploadButton.configure(text="Choose an Image", fg_color="orange", hover_color="dark orange")
    
    
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
        ChildWindow.geometry("400x350")
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
        
ItemNameLabel = customtkinter.CTkLabel(InputFieldFrame, font=global_font, width=590, text="Item Name")
ItemNameLabel.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
ItemNameInput = customtkinter.CTkEntry(InputFieldFrame, font=global_font, width=590)
ItemNameInput.grid(row=1, column=1, padx=(10, 10), pady=10, columnspan=2)

LocationLabel = customtkinter.CTkLabel(InputFieldFrame, font=global_font, width=590, text="Location Found")
LocationLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
LocationInput = customtkinter.CTkEntry(InputFieldFrame, font=global_font, width=590)
LocationInput.grid(row=3, column=1, padx=(10, 10), pady=10, columnspan=2)

DateLabel = customtkinter.CTkLabel(InputFieldFrame, font=global_font, width=590, text="Date Found")
DateLabel.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
DateInput = customtkinter.CTkButton(InputFieldFrame, text=DateSelection.get(), font=global_font, command=OpenWindow, width=590)
DateInput.grid(row=5, column=1, padx=(10, 10), pady=10, columnspan=2)

InputFieldFrame.grid_rowconfigure(0, weight=1)

SubmitButton = customtkinter.CTkButton(InputFieldFrame, text="Add Item", font=global_font, fg_color="green", hover_color="dark green", width=250, command=Submit)
SubmitButton.grid(column=1, row=6, padx=(10, 0), pady=10)
ResetButton = customtkinter.CTkButton(InputFieldFrame, text="Reset", font=global_font, fg_color="red", hover_color="dark red", width=250, command=Reset)
ResetButton.grid(row=6, column=2, padx=(0, 10), pady=10)


InputFieldFrame.grid_propagate(False)

##### Image Input Frame #####

def SelectImage():
    global img
    global filedir
    cur_dir = os.getcwd()
    cur_dir += "\Images"
    filedir = filedialog.askopenfilename(title="Select Image")
    shutil.copy(filedir, cur_dir)
    
    img = customtkinter.CTkImage(light_image=Image.open(filedir), size=(300, 300))
    ImageLabel.configure(image=img)
    UploadButton.configure(text=filedir, fg_color="orange", hover_color="dark orange")

InputFieldFont = customtkinter.CTkFont(family="MS Sans Serif", size=20)

Information = """\nWelcome to Admin Application\n\nYou may submit a new \n\nlost item by providing the\n\nfollowing details in the fields"""

InformationLabel = customtkinter.CTkLabel(ImageInputFrame, width=300, text=Information, font=InputFieldFont)
InformationLabel.grid(row=0, column=0)

ImageLabel = customtkinter.CTkLabel(ImageInputFrame, width=300, height=300, text="")
ImageLabel.grid(row=0, column=1, rowspan=3)

InputFieldFrame.grid_rowconfigure(1, weight=1)

UploadButton = customtkinter.CTkButton(ImageInputFrame, width=250, height=75, text="Choose an Image", fg_color = "orange", hover_color="dark orange", font=InputFieldFont, command=SelectImage)
UploadButton.grid(row=2, column=0)

SecurityOptions = ["High", "Low"]
SecurityChoice = StringVar(value="Low")
SecurityLabel = customtkinter.CTkLabel(ImageInputFrame, text="Security Level", font=global_font)
SecurityLabel.grid(row=3, column=0, sticky=N+S+W+E)
SecurityInput = customtkinter.CTkOptionMenu(ImageInputFrame, values=SecurityOptions, variable=SecurityChoice, font=global_font)
SecurityInput.grid(row=3, column=1, sticky=N+S+W+E)

ImageInputFrame.grid_propagate(False)

##### Colour Select Frame #####

ColourDict = {}
Colours = ["Black", "White", "Red", "Green", "Blue", "Pink", "Brown", "Yellow", "Orange", "Purple"]

ColourLabel = customtkinter.CTkLabel(ColourSelectFrame, font=global_font, text="Select all that apply.").grid(row=0, column=0)

for i in range(len(Colours)):
    ColourDict[i] = IntVar(value=0)
    CheckBox1 = customtkinter.CTkCheckBox(ColourSelectFrame, text=Colours[i], checkbox_width=400, checkbox_height=50, font=global_font, variable=ColourDict[i], onvalue=1, offvalue=0)
    CheckBox1.grid(row=i+1, column=0, sticky=N+S+W+E)

##### Type Select Frame #####
TypeSelection = StringVar(value="Misc")
Types = ["Bottle", "Backpack", "Uniforms/Shirts", "Uniforms/Belts", "Uniforms/Pants", "Uniforms/Hoodies", "Stationaries/Pencil Case", "Stationaries/Calculators", "Valuables/Phones", "Valuables/Laptops", "Valuables/Watches"]

TypeLabel = customtkinter.CTkLabel(TypeSelectionFrame, font=global_font, text="Select one.").grid(row=0, column=0)

for i in range(len(Types)):
    if "/" in Types[i]:
        DisplayString = (Types[i].split("/"))[1]
    else:
        DisplayString = Types[i]
    
    CheckBox2 = customtkinter.CTkRadioButton(TypeSelectionFrame, text=DisplayString, radiobutton_width=400, radiobutton_height=50, font=global_font, variable=TypeSelection, value=Types[i])
    CheckBox2.grid(row=i+1, column=0, sticky=N+S+W+E)
    
#############################
InputFieldFrame.grid(row=0, column=0)
ColourSelectFrame.grid(row=1, column=0)
ImageInputFrame.grid(row=0, column=1)
TypeSelectionFrame.grid(row=1, column=1)

root.mainloop()
