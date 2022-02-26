###############################
# TITLE : GUI  - tkinter - layout
# CREATE DATE : 2022-02-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

windows = Tk()
windows.title("Layout manager")

btn1 = Button(windows, text="Button1", bg ="yellow", fg = "blue", width=50, height=10)
btn2 = Button(windows, text="Button2", bg ="yellow", fg = "blue", width=50, height=10)
btn3 = Button(windows, text="Button3", bg ="yellow", fg = "blue", width=50, height=10)

# pack
# btn1.pack()
# btn2.pack()

# side = TOP, BOTTOM, RIGHT, LEFT
btn1.pack(side=LEFT, padx=20, pady=10)
btn2.pack(side=LEFT, padx=20, pady=10)
btn3.pack(side=LEFT, padx=20, pady=10)

# padx(padding - x )
# pady(padding - y)

btn1["text"] = "_ONE"
btn2["text"] = "_TWO"
btn3["text"] = "_THREE"
windows.mainloop()