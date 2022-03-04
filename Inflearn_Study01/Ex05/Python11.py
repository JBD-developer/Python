###############################
# TITLE : GUI  - label
# CREATE DATE : 2022-02-28
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-03-01
# VERSION : 1.0.0
###############################

from tkinter import *

# label

root = Tk()
photo = PhotoImage(file="E:\\workSpace_Etc\\index.png")
lbl = Label(root, image=photo)
lbl.photo = photo
lbl.pack()
root.mainloop()
