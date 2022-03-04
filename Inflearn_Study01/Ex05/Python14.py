###############################
# TITLE : GUI  - entry
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import tkinter as tk
# Entry
def show():
    print("Name : %s\nAge : %s" %(e1.get(), e2.get()))


windows = tk.Tk()
tk.Label(windows, text="name").grid(row=0, column=0)
tk.Label(windows, text="age").grid(row=1, column=0)

e1 = tk.Entry(windows)
e2 = tk.Entry(windows)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(windows, text="Hide", command=windows.quit).grid(row=2, column=0, sticky = "W", pady=5)
tk.Button(windows, text="Show", command=show).grid(row=2, column=1, pady=5, sticky = "W")

windows.title("Entry")



windows.mainloop()