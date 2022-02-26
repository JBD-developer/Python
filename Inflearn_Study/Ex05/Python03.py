###############################
# TITLE : GUI  - tkinter - event
# CREATE DATE : 2022-02-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *
counter = 0


def btn_click0():
    btn1["text"] = "click"


def btn_click1():
    global counter
    counter += 1
    btn1["text"] = "Plus" + str(counter)


def btn_click2():
    global counter
    counter = 0
    btn1["text"] = "Plus" + str(counter)


if __name__ == "__main__":
    windows = Tk()
    windows.title("Event")

    btn1 = Button(windows, text="Plus", bg="yellow", fg="blue", width=20, height=20, command=btn_click1)
    btn2 = Button(windows, text="Reset", bg="yellow", fg="blue", width=20, height=20, command=btn_click2)

    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)

    windows.mainloop()