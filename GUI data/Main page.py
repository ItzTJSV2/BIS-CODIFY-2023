import base64
from io import BytesIO

from PIL import Image
import PySimpleGUI as sg

import tkinter

sg.theme("DarkAmber")
sg.set_options(font=("Courier New", 16))

text = "tags"
column = [[sg.Text(text, font=("Courier New", 16))]]



# Get size of image `sg.EMOJI_BASE64_HAPPY_BIG_SMILE`
buffer = BytesIO(base64.b64decode(sg.EMOJI_BASE64_HAPPY_BIG_SMILE))
im1 = Image.open(buffer)
width, height = im1.size

# Create a blank image
im2 = Image.new("RGBA", (width, height), "#ffffff00")
with BytesIO() as output:
    im2.save(output, format="PNG")
    blank = output.getvalue()

# Image state of button saved in `element.metadata`
layout = [
    [[sg.Button("", image_data=blank, key=(j, i), metadata=False) for i in range(1)] for j in range(1)]], [sg.Column(column, size=(800, 300), scrollable=True, key = "Column")], [sg.OK(), sg.Button('Up', key = "up"), sg.Button('Down', key = "down")]
    
window = sg.Window("Title", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    elif type(event) == tuple:
        element = window[event]
        if element.metadata:
            element.update(image_data=blank)
        else:
            element.update(image_data=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
        element.metadata = not element.metadata
    elif event == "down":
        window['Column'].Widget.canvas.yview_moveto(1.0)
    elif event == "up":
        window['Column'].Widget.canvas.yview_moveto(0.0)

window.close()