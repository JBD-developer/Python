###############################
# TITLE : GUI  - tkinter - widget
# CREATE DATE : 2022-02-27
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

windows = Tk()
windows.title("Entry Widget")
windows.geometry("600x500")
frame = Frame(windows)

btn1 = Button(frame, text="Button1", bg="red", fg="white" , width=10, height=5)
btn2 = Button(frame, text="Button2", bg="green", fg="white", width=10, height=5)
btn3 = Button(frame, text="Button3", bg="yellow", fg="white" , width=10, height=5)

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)

label = Label(windows, text="Label")
label.pack()
frame.pack()
windows.mainloop()