###############################
# TITLE : GUI  - text
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import tkinter as tk

root = tk.Tk()
root.title("Text")
root.geometry("500x400")
txt = tk.Text(root, height=10, width=500)
txt.insert(tk.END, "The text widget can represent multiple lines of text.")
txt.pack()
root.mainloop()