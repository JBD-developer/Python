###############################
# TITLE : GUI  - canvas
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *
import random
"""
windows = Tk()
windows.title("Canvas")
# windows.geometry("700x700")

canvas = Canvas(windows, width=500, height=500, bg="white")
canvas.pack()

# draw line
line1 = canvas.create_line(0, 0, 500, 500, fill="blue")
line2 = canvas.create_line(0, 500, 500, 0, fill="red", width=5)


# draw rectangle
rec1 = canvas.create_rectangle(50, 50, 200, 200, fill="yellow")
rec2 = canvas.create_rectangle(300, 300, 350, 350, fill="blue", outline="red", width=10)

# coords() change position
# itemconfig() change color
# delete()
canvas.coords(line1, 250, 250, 500, 500)
canvas.itemconfig(line2, fill="black")
windows.mainloop()
"""
"""
windows = Tk()
windows.title("Draw")

canvas = Canvas(windows, width=600, height=500, bg="white")
canvas.pack()
color = ["red", "orange", "black", "blue", "yellow", "violet", "green"]

def draw_rect():
    canvas.delete(ALL)
    x = random.randint(1, 600)
    y = random.randint(1, 500)
    w = random.randrange(100)
    h = random.randrange(100)

    canvas.create_rectangle(x, y, w, h, fill=random.choice(color))

# for i in range(10):
#     draw_rect()

button = Button(windows, text="Rectangle", width=20, height=5, command=draw_rect)
button.pack()
windows.mainloop()
"""


class Shape():
    def __init__(self):
        windows = Tk()
        windows.title("Draw Square")

        self.canvas = Canvas(windows, width=600, height=400, bg="white")
        self.canvas.pack()

        # frame = Frame(windows, width=600, height=400, bg ="black")
        frame = Frame(windows)
        frame.pack()

        btnRectangle = Button(frame, text="Rectangle" , command=self.draw_rectangle)
        btnOval = Button(frame, text="Oval", command=self.draw_oval)
        btnArc = Button(frame, text="Arc", command=self.draw_arc)
        btnPolygon = Button(frame, text="Polygon", command=self.draw_polygon)
        btnLine = Button(frame, text="Line", command=self.draw_line)
        btnCharacter = Button(frame, text="Character", command=self.draw_character)
        btnClear = Button(frame, text="Clear", command=self.draw_clear())

        btnRectangle.grid(row=0, column=1)
        btnOval.grid(row=0, column=2)
        btnArc.grid(row=0, column=3)
        btnPolygon.grid(row=0, column=4)
        btnLine.grid(row=0, column=5)
        btnCharacter.grid(row=0, column=6)
        btnClear.grid(row=0, column=7)

        windows.mainloop()

    def draw_rectangle(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")
        print("draw_Rectangle")

    def draw_oval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")
        print("draw_Oval")

    def draw_arc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0, extent=90 , tags="arc")
        print("draw_Arc")

    def draw_polygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, fill="blue", tags="polygon")
        print("draw_Polygon")

    def draw_line(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=5, arrow ="last", activefill="black", tags="line")
        print("draw_Line")

    def draw_character(self):
        self.canvas.create_text(60, 40, text="Character", font="Times 10 bold underline", tag="Character")

    def draw_clear(self):
        self.canvas.delete(ALL)



if __name__ == "__main__":
    shape = Shape()