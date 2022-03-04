###############################
# TITLE : GUI  - tkinter - widget
# CREATE DATE : 2022-02-27
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *
from tkinter.colorchooser import askcolor

windows = Tk()
windows.title("Color")
btn = Button(windows, text="click")
btn.pack()

# btn["fg"] = "yellow"
# btn["bg"] = "green"

btn["fg"] = "#4287f5"
btn["bg"] = "#254194"

# tkinter.colorchooser askcolor()

color = askcolor()
print(color)
print(type(color))
btn["fg"] = color[1]


color = askcolor()
print(color)
print(type(color))
btn["bg"] = color[1]

windows.mainloop()