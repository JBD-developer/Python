###############################
# TITLE : GUI  - label
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import tkinter as tk


class Test1:
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.geometry("200x80")
        self.label = tk.Label(self.windows, text ="Label")
        self.btn = tk.Button(self.windows, text ="Read", command=self.read_label_text())

        self.btn.pack()
        self.label.pack()
        self.windows.mainloop()

    def read_label_text(self):
        print(self.label.cget("text"))

# lbl1 = Label(windows, text="Label1", fg="red", font="고딕체 32 bold italic").pack()
# lbl2 = Label(windows, text="Label2", fg="blue", font="궁서체 32 bold italic").pack()

class Test2:
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.geometry("200x80")
        self.label = tk.Label(self.windows, text="Label")
        self.btn = tk.Button(self.windows, text="Read", command=self.read_label_text)

        self.btn.pack()
        self.label.pack()
        self.windows.mainloop()

    def read_label_text(self):
        print(self.label["text"])

class Test3:
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.geometry("200x80")
        self.text = tk.StringVar()
        self.text.set("Label")
        self.label = tk.Label(self.windows, textvariable=self.text)
        self.btn = tk.Button(self.windows, text="Read", command=self.read_label_text)

        self.btn.pack()
        self.label.pack()
        self.windows.mainloop()

    def read_label_text(self):
        print(self.label["text"])

if __name__ == "__main__":
     test = Test3()
