###############################
# TITLE : GUI  - tkinter - widget
# CREATE DATE : 2022-02-27
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *
from tkinter import font

class App:
    def __init__(self):
        roots = Tk()
        roots.title("Font")
        self.customFont = font.Font(family="Helvetica", size=12)

        btnFrame = Frame()
        label = Label(roots, text="Hello world", font=self.customFont)
        btnFrame.pack()
        label.pack()

        btn1 = Button(roots, text="Big", command=self.font_big)
        btn2 = Button(roots, text="Small", command=self.font_small)
        btn1.pack()
        btn2.pack()
        roots.mainloop()

    def font_big(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.configure(size=size+2)

    def font_small(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.configure(size=size - 2)


if __name__ == "__main__":
    app = App()