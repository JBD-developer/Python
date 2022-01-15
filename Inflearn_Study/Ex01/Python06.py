###############################
# TITLE : Control Statement
# CREATE DATE : 2022-01-11
# CREATOR : J
# MODIIFIER : J
# MODIFY DATE : 2022-01-15
# VERSION : 1.0.0
###############################
import turtle

# Python if ~ else 50%
score = 60
if score > 58:
    print("C+")
else:
    print("D")

age = int(input("Your age? \nAge : "))
if age >= 19:
    print("Adult")
else:
    print("Children")

gender = input("Your Gender? F, M\nGender : ")
if gender == "M":
    print("Male")
else:
    print("Female")

# Python bool True! False!

flag = bool(input())
print(type(flag))
if flag:
    print(True)
else:
    print(False)

flag = not flag
print(flag)

t = turtle.Pen()

while(True):

    direction = input("Left : L Right R Exit : Q\n")
    if direction == "Q":
        print("Exit")
        break

    if direction == "L":
        print("Input L")
        t.left(60)
        t.forward(50)

    if direction == "R":
        print("Input R")
        t.right(60)
        t.forward(50)

turtle.exitonclick()

numX = float(input("Weight of luggage \nWeight:"))

if numX > 20.0:
    print("An additional 20,000")
else:
    print("Free")

numX = int(input("Enter the integer"))
if numX == 0:
    print("Zero")
elif numX % 2 == 0:
    print("even numbers")
elif numX % 2 == 1:
    print("odd numbers")

numX = int(input("Enter the integer \nX:"))
numY = int(input("Enter the integer \nY:"))
numMax = 0
if numX > numY:
    numMax = numX
else:
    numMax = numY

print("Max value : ", numMax)