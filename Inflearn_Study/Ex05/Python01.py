###############################
# TITLE : GUI  - tkinter
# CREATE DATE : 2022-02-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

windows = Tk() # root

label = Label(windows, text="Hello World TK Interface")
btn1 = Button(windows, text="Button1", bg="yellow", fg="blue", width=80, height=20, font="고딕, 15")
btn2 = Button(windows, text="Button2")
label.pack()
btn1.pack(side=LEFT, padx=10)
btn2.pack(side=LEFT, padx=10)
btn1["text"] = "Button1"
btn2["text"] = "Button2"
windows.mainloop()