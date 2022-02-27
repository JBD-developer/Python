###############################
# TITLE : GUI  - tkinter - widget
# CREATE DATE : 2022-02-27
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *
"""
 Button
 Canvas
 Checkbutton
 Entry
 Frame
 Label
 Listbox
 Menu
 Menubutton
 Message
 Rediobutton
"""

# Entry
windows = Tk()
windows.title("Entry Widget")
windows.geometry("400x200")
entry = Entry(windows, fg="black", bg="yellow", width=80)
# entry.pack()

# pack

# btn1 = Button(windows, text="box1", bg="red", fg="white").pack()
# btn2 = Button(windows, text="box2", bg="green", fg="white").pack()
# btn3 = Button(windows, text="box3", bg="blue", fg="white").pack()

# grid

# btn1 = Button(windows, text="box1", bg="red", fg="white").grid(row=0, column=0)
# btn2 = Button(windows, text="box2", bg="green", fg="white").grid(row=0, column=1)
# btn3 = Button(windows, text="box3", bg="blue", fg="white").grid(row=1, column=0)
# btn4 = Button(windows, text="box4", bg="yellow", fg="white").grid(row=1, column=1)


# place
btn1 = Button(windows, text="box1", bg="red", fg="white").place(x=10, y=10)
btn2 = Button(windows, text="box2", bg="green", fg="white").place(x=100, y=50)
btn3 = Button(windows, text="box3", bg="blue", fg="white").place(x=10, y=100)
btn4 = Button(windows, text="box4", bg="yellow", fg="white").place(x=200, y=50)


windows.mainloop()
