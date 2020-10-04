import time
import subprocess
from PIL import Image, ImageTk, ImageDraw, ImageFont
import keyboard
import string
import curses
import sys
from os import listdir

import tkinter as tk
from tkinter import Frame

#from tkinter import *
#from tkinter.ttk import *

# globals?
root = None
myCanvas = None
text = None

img = None

key_pressed = None
key_released = None

mode = ''

stack = []

quit = False

# ?
class Display:
    """class to hold 'display' specs"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

# http://www.effbot.org/tkinterbook/tkinter-application-windows.htm
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


# application class?
class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


disp = Display(128, 32)

# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()
# font = ImageFont.truetype('minecraftia.ttf',8)


image = Image.open(r'piskel.png')
image = image.convert('1')

#MAIN

def main():
    global root
    global mode
    global stack
    global image
    global img

    setup_tk()

    setup_display()

    keyboard.on_press(handleKeyPress)
    keyboard.on_release(handleKeyRelease)

    # push initial
    img = ImageTk.PhotoImage(image)

    stack.append("splash")
    mode = stack[0] if len(stack) == 1 else stack[len(stack) - 1]
    show( mode )

    root.mainloop()


#FUNCTIONS

def setup_tk():
    global root

    # init tk
    root = tk.Tk(className='AlphaPi Emulator')
    root.geometry("256x64")

    # create a menu -- http://www.effbot.org/tkinterbook/tkinter-application-windows.htm
    menu = tk.Menu(root)
    root.config(menu=menu)

    filemenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=exit_callback)

    helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=about_callback)

    # create a statusbar -- http://www.effbot.org/tkinterbook/tkinter-application-windows.htm
    status = StatusBar(root)
    status.pack(side=tk.BOTTOM, fill=tk.X)


def setup_display():
    global root
    global myCanvas

    global height
    global width

    # create canvas
    myCanvas = tk.Canvas(root, bg="black", height=height, width=width)

    # add to window and show
    myCanvas.pack()


def about_callback():
    print("called the callback!")


def exit_callback():
    sys.exit(0)


def handleKeyPress(kbdEvent):
    global key_pressed
    key_pressed = kbdEvent.name

    print("pressed " + key_pressed)

    input_handler()


def handleKeyRelease(kbdEvent):
    global key_released
    key_released = kbdEvent.name


def input_handler():
    global root
    global mode
    global stack
    global myCanvas
    global quit

    #mode = '' if len(stack) == 0 else stack[0]
    #mode = mode if len(stack) == 1 else stack[len(stack) - 1]
    mode = stack[0] if len(stack) == 1 else stack[len(stack) - 1]

    print("-- before")
    print("stack is: " + ','.join(stack))
    print("mode is: " + mode)

    if mode == 'splash':
        if (key_pressed == "enter"):
            stack.append("main_menu")
    elif mode == 'main_menu':
        if (key_pressed == "1"):
            stack.append("wordprocessor_menu") # go to wordprocessor_menu
        elif (key_pressed == "2"):
            #backup_files()
            pass
        elif (key_pressed == "3"):
            print('And the number shall be 3!')
            root.destroy()
            sys.exit(0)
    elif mode == 'wordprocessor_menu':
        if (key_pressed == "1"):
            pass
        elif (key_pressed == "2"):
            pass
        elif (key_pressed == "3"):
            stack.append("wordprocessor_help") # go to wordprocessor_help
        elif(key_pressed == "esc"):
            stack.pop()  # go back
    elif mode == 'wordprocessor_help':
        if (key_pressed == "esc"):
            stack.pop()  # go back
    
    #mode = '' if len(stack) == 0 else stack[0]
    #mode = mode if len(stack) == 1 else stack[len(stack) - 1]
    mode = stack[0] if len(stack) == 1 else stack[len(stack) - 1]

    print("-- after")
    print("stack is: " + ','.join(stack))
    print("mode is: " + mode)

    show( mode )


def splash():
    global myCanvas

    global img

    myCanvas.create_image(3, 3, anchor="nw", image=img)
    myCanvas.create_rectangle((2, 2, 129, 33), outline="white")

    myCanvas.pack()
    myCanvas.update_idletasks()


def main_menu():
    global myCanvas

    myCanvas.delete(tk.ALL)

    myCanvas.create_text(x+3, top+0,   anchor="nw", fill="white", text="1. Word Processor", width="128")
    myCanvas.create_text(x+3, top+10,  anchor="nw", fill="white", text="2. Backup Files", width="128")
    myCanvas.create_text(x+3, top+20,  anchor="nw", fill="white", text="3. Quit", width="128")
    myCanvas.create_rectangle((2, 2, 129, 33), outline="white")
   
    myCanvas.pack()
    myCanvas.update_idletasks()


def wordprocessor_menu():
    global myCanvas

    myCanvas.delete(tk.ALL)

    myCanvas.create_text(x+3, top+0,   anchor="nw", fill="white", text="1. Create new file", width="128")
    myCanvas.create_text(x+3, top+10,  anchor="nw", fill="white", text="2. Edit existing file", width="128")
    myCanvas.create_text(x+3, top+20,  anchor="nw", fill="white", text="3. Help", width="128")
    myCanvas.create_rectangle((2, 2, 129, 33), outline="white")
    
    myCanvas.pack()
    myCanvas.update_idletasks()


def wordprocessor_help():
    global myCanvas

    myCanvas.delete(tk.ALL)

    myCanvas.create_text(x+3, top+0,   anchor="nw", fill="white", text="Ctrl + S to save", width="128")
    myCanvas.create_text(x+3, top+10,  anchor="nw", fill="white", text="'Esc' to go back", width="128")
    myCanvas.create_text(x+3, top+20,  anchor="nw", fill="white", text="Ex file: test.txt", width="128")
    myCanvas.create_rectangle((2, 2, 129, 33), outline="white")

    myCanvas.pack()
    myCanvas.update_idletasks()


def show(str):
    dispatcher[str]()


dispatcher = {
    'splash': splash,
    'main_menu': main_menu,
    'wordprocessor_menu': wordprocessor_menu,
    'wordprocessor_help': wordprocessor_help
}

# Start
main()