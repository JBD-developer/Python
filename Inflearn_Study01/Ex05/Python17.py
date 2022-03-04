###############################
# TITLE : GUI  - calculator
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from tkinter import *

def btn_click(key):
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.insert(END, "=" +s)
    elif key == "C":
        display.delete(0, END)
    else:
        display.insert(END, key)

root = Tk()
root.title("Calculator")
display = Entry(root, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = ["7", "8", "9", "/", "C",
               "4", "5", "6", "*", " ",
               "1", "2", "3", "-", " ",
               "0", ".", "=", "+", " "]

row_index = 1
col_index = 0

for button_text in button_list:
    Button(root, text=button_text, width=5, command=lambda t=button_text: btn_click(t)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0





root.mainloop()