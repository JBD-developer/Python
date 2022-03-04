###############################
# TITLE : GUI  - label
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

root = Tk()
root.title("Label")

photo = PhotoImage(file="E:\\workSpace_Etc\\index.png")
lbl = Label(root, image=photo)
lbl.photo = photo
lbl.pack(side=RIGHT)
msg = "Life is too short! You nedd Python!"

lbl2 = Label(root, justify=LEFT, padx=10, text=msg).pack(side=LEFT)

root.mainloop()