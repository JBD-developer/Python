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
windows.geometry("300x300")
Label(windows, text="화씨").grid(row=0, column=0)
Label(windows, text="섭씨").grid(row=1, column=0)

e1 = Entry(windows).grid(row=0, column=1)
e2 = Entry(windows).grid(row=1, column=1)

Button(windows, text="Change").grid(row=2, column=1)

windows.mainloop()