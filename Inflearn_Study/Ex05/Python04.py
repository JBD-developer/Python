###############################
# TITLE : GUI  - tkinter - event
# CREATE DATE : 2022-02-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

class App:
    def __init__(self):
        windows = Tk()
        helloB = Button(windows, text="Hello", command=self.hello_click, fg="red")
        helloB.pack(side=LEFT)
        quitB = Button(windows, text="Quit", command=self.quit_click)
        quitB.pack(side=LEFT)
        windows.mainloop()

    def hello_click(self):
        print("Button hello click")

    def quit_click(self):
        print("Button quit click")


if __name__ == "__main__":
    app = App()

