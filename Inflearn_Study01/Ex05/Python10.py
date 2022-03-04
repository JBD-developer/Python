###############################
# TITLE : GUI  - tkinter - widget
# CREATE DATE : 2022-02-27
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *


class App:
    def __init__(self):
        root = Tk()
        Label(root, text="Width").grid(row=0)
        Label(root, text="Height").grid(row=1)

        e1 = Entry(root).grid(row=0, column=1)
        e2 = Entry(root).grid(row=1, column=1)

        photo = PhotoImage(file="E:\\workSpace_Etc\\index.png")
        label = Label(root, image=photo)
        label.grid(row=0, column=2, columnspan=2, rowspan=2)

        btn1 = Button(root, text="Button1").grid(row=2, column=0, columnspan=2)
        btn2 = Button(root, text="Big").grid(row=2, column=2)
        btn3 = Button(root, text="Small").grid(row=2, column=3)

        root.mainloop()


if __name__ =="__main__":
    app = App()
