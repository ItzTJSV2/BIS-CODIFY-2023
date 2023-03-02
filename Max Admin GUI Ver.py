from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import os
import shutil
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from datetime import date

from addnSearch import *

TagDict = {}  # This will store all the tags' values


def UploadImage():
    global img
    global filedir
    cur_dir = os.getcwd()
    cur_dir += "\Images"
    filedir = filedialog.askopenfilename(title="Select Image")
    shutil.copy(filedir, cur_dir)
        
    img = Image.open(filedir)
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    ShowImage['image'] = img
    UploadButton['text']= f"{filedir}"
    UploadButton['bg'] = "#f0f0f0"

def Submit():
    Tags = []
    if ItemNameEntry.get() == "":
        ItemNameLabel['bg'] = "#f00"
        return
    else:
        ItemNameLabel['bg'] = "#f0f0f0"
        
    if LocationEntry.get() == "":
        LocationLabel['bg'] = "#f00"
        return
    else:
        LocationLabel['bg'] = "#f0f0f0"
    
    if ShowImage['image'] != "":
        UploadButton['bg'] = "#f0f0f0"
    else:
        UploadButton['bg'] = "#f00"
        return
            
    if clicked.get() == "":
        SecurityLabel['bg'] = "#f00"
        return
    else:
        SecurityLabel['bg'] = "#f0f0f0"
        
    TagArray = []
    for i in range(len(TagDict)):
        if TagDict[i].get() == 1:
            TagArray.append(i)
    
    # Calendar will default to today
    # Tags are optional
    # Security will default to Low
    # Rest have defaults of False
    addItem(ItemNameEntry.get(), LocationEntry.get(), f"Images\{os.path.basename(filedir)}", str(CalendarEntry.get_date()), TagArray, clicked.get())
    Reset()
    
def Reset():
    print("Reset UI")
    clicked.set("")
    ShowImage['image'] = ""
    ItemNameEntry.delete(0, END)
    LocationEntry.delete(0, END)
    filedir = ""
    CalendarEntry.delete(0, "end")
    for i in range(len(TagDict)):
        TagDict[i].set(0)
    UploadButton['text']= "Open Image"
    SecurityLabel['bg'] = "#f0f0f0"
    
    
gui = Tk()
ImageFrame = Frame(gui, width=50, height=300)
InputFieldsFrame = Frame(gui)
TagsFrame = Frame(gui, width=50, height=100)
ControlFrame = Frame(gui)

gui.title("Admin Interface")
gui.geometry("1920x1080")


ShowImage = Label(ImageFrame)
UploadButton = Button(ImageFrame, text="Open Image", command=UploadImage, fg='blue', font=('verdana', 16))

SubmitButton = Button(ControlFrame, text="Submit", command=Submit, fg='blue', font=('verdana', 16))
ResetButton = Button(ControlFrame, text="Reset", command=Reset, fg='red', font=('verdana', 16))

Information = Label(ImageFrame, font=('verdana', 16), text="Welcome!\nThis is the Admin Page.")

ItemNameEntry = Entry(InputFieldsFrame, width=50, font=('verdana', 16))
ItemNameLabel = Label(InputFieldsFrame, font=('verdana', 16), text="Item Name")

LocationEntry = Entry(InputFieldsFrame, width=50, font=('verdana', 16))
LocationLabel = Label(InputFieldsFrame, font=('verdana', 16), text="Location Found")

CalendarEntry = DateEntry(InputFieldsFrame, width=50, font=('verdana', 16), selectmode='day', maxdate=date.today())
CalendarLabel = Label(InputFieldsFrame, font=('verdana', 16), text="Date Found")
CalendarEntry.delete(0, "end")

Levels = ["High", "Low"]
clicked = StringVar()
clicked.set("")

BooleanSecurity = OptionMenu(InputFieldsFrame, clicked, *Levels)
SecurityLabel = Label(InputFieldsFrame, font=('verdana', 16), text="Security Level")

# TAGS SECTION
ScrollableBar = Scrollbar(TagsFrame, orient="vertical")
TagBox = Text(TagsFrame, width=20, height=10, yscrollcommand=ScrollableBar.set)
ScrollableBar.config(command=TagBox.yview)
ScrollableBar.pack(side="right", fill="y")
TagBox.pack(side="left")  

NamedTags = ["Test", "bruh", "LUL"] # Change later

for i in range(len(NamedTags)):
    TagDict[i] = IntVar()
    CheckBox = Checkbutton(TagsFrame, font=('verdana', 16), text=f"{NamedTags[i]}", variable=TagDict[i], onvalue=1, offvalue=0)
    TagBox.window_create("end", window=CheckBox)
    TagBox.insert("end", "\n")


ImageFrame.pack()
InputFieldsFrame.pack()
TagsFrame.pack()
ControlFrame.pack()

Information.grid(row=0, column=0)
ShowImage.grid(row=0, column=1)
UploadButton.grid(row=1, column=0)

ItemNameEntry.grid(row=0, column=0)
ItemNameLabel.grid(row=0, column=1)

LocationEntry.grid(row=1, column=0)
LocationLabel.grid(row=1, column=1)

CalendarEntry.grid(row=2, column=0)
CalendarLabel.grid(row=2, column=1)

BooleanSecurity.config(width=50, font=('verdana', 16))
BooleanSecurity.grid(row=3, column=0)
SecurityLabel.grid(row=3, column=1)

SubmitButton.grid(row=0, column=0)
ResetButton.grid(row=0, column=1)

gui.mainloop()