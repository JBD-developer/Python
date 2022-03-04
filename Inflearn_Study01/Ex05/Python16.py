###############################
# TITLE : GUI  - guess
# CREATE DATE : 2022-03-01
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import tkinter as tk
import random

answer = random.randint(1,100)
# print("Random number" answer)

def try_number():
    guess = int(guessField.get())
    msg = ""
    if guess > answer:
        print("Big")
        msg ="Big"
    elif guess < answer:
        print("Small")
        msg = "Small"
    else:
        mag = "Correct "
        print("correct answer")

    resultLabel["text"] = msg

def reset_number():
    answer = random.randint(1, 100)
    resultLabel["text"] = "Challenge"
    print()

windows = tk.Tk()
windows.title("Guess Game")
windows.geometry("500x80")
windows.configure(bg="white")

titleLabel = tk.Label(windows, text="Welcome guess game").pack()
guessField = tk.Entry(windows)
guessField.pack(side=tk.LEFT)

tryButton = tk.Button(windows, text="Challenge", fg="green", bg="white", command=try_number).pack(side=tk.LEFT)
resetButton = tk.Button(windows, text="Reset", fg="red", bg="white", command=reset_number).pack(side=tk.LEFT)


resultLabel = tk.Label(windows, text="Please enter a number between 1 and 100", bg="white")
resultLabel.pack(side=tk.LEFT)
windows.mainloop()
