###############################
# TITLE : Control Statement
# CREATE DATE : 2022-01-11
# CREATOR : J
# MODIIFIER : J
# MODIFY DATE : 2022-01-16
# VERSION : 1.0.0
###############################
import turtle
from random import *

# Python if ~ else 50%
# score = 60
# if score > 58:
#     print("C+")
# else:
#     print("D")
#
# age = int(input("Your age? \nAge : "))
# if age >= 19:
#     print("Adult")
# else:
#     print("Children")
#
# gender = input("Your Gender? F, M\nGender : ")
# if gender == "M":
#     print("Male")
# else:
#     print("Female")
#
# # Python bool True! False!
#
# flag = bool(input())
# print(type(flag))
# if flag:
#     print(True)
# else:
#     print(False)
#
# flag = not flag
# print(flag)
#
# t = turtle.Pen()
#
# while(True):
#
#     direction = input("Left : L Right R Exit : Q\n")
#     if direction == "Q":
#         print("Exit")
#         break
#
#     if direction == "L":
#         print("Input L")
#         t.left(60)
#         t.forward(50)
#
#     if direction == "R":
#         print("Input R")
#         t.right(60)
#         t.forward(50)
#
# turtle.exitonclick()
#
# numX = float(input("Weight of luggage \nWeight:"))
#
# if numX > 20.0:
#     print("An additional 20,000")
# else:
#     print("Free")
#
# numX = int(input("Enter the integer"))
# if numX == 0:
#     print("Zero")
# elif numX % 2 == 0:
#     print("even numbers")
# elif numX % 2 == 1:
#     print("odd numbers")
#
# numX = int(input("Enter the integer \nX:"))
# numY = int(input("Enter the integer \nY:"))
# numMax = 0
# if numX > numY:
#     numMax = numX
# else:
#     numMax = numY
#
# print("Max value : ", numMax)
#
# total_price = int(input("Enter the Total Price : \n"))
#
# if total_price > 50000:
#     discount_price = total_price * 0.05
#     sales_price = total_price - discount_price
#     print("Purchase amount.", total_price)
#     print("Discount amount.", discount_price)
#     print("Sale amount", sales_price)
# else:
#     print("It's not eligible for discount")
#
#
# message = input("Enter the message")
#
# iLength = len(message)
#
# if iLength % 2 == 0:
#     print("Even numbers")
#     ch0 = message[iLength // 2 - 1]
#     ch1 = message[iLength // 2]
#     print(ch0, ch1)
# else:
#     ch2 = message[iLength//2]
#     print(ch2)
#     print("Odd numbers")
#
# # Logical operator
#
# name = "Python"
# version = 3.8
# language = "Interpreter"
#
# if (name == "Python") & (version >= 3.7):
#     print("Python")
# else:
#     print("Other language")
#
# if not(1 == 0):
#     print(True)
# else :
#     print(False)
#
# grade1 = float(input("Please enter your grade"))
# grade2 = float(input("Enter your grades that you completed"))
#
# if (grade1 >= 140.0) & (grade2 >= 2.0):
#     print("Success")
# else:
#     print("Failure")
#
# weight = float(input("Your weight"))
# height = float(input("Youur height"))
# height /= 100.0
# numBMI = weight / (height * height )
# print("BMI :", numBMI)
#
# if (numBMI >= 20.0) & (numBMI < 25.0):
#     print("Standard")
# else:
#     print("Weight management is necessary.")

# if ~ elif
#score = int(input("Your score 0~100\n"))
# score = 50
# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# elif score >= 60:
#     print("Grade D")
# else:
#     print("F")
#
# # nested  if elif
#
# applyQuality = input("Apple satus Good, Bad\n")
# applePrice = int(input("Apple Price\n"))
#
# if applyQuality == "Good":
#     if applePrice < 1000:
#         print("Buy 10 apples")
#     else :
#         print("Buy 5 apples")
# else:
#     print("I don't buy apples")
#
# numX = int(input("Enter the integer"))
#
# if numX == 0:
#     print("Zero")
# elif numX > 0:
#     print("positive number")
# else:
#     print("negative number")

# randint(a, b) a ~ b 까지의 사이에 있는 정수를 반환
numRandom1 = randint(1, 6)
print(numRandom1)

# random() 함수는 0.0 ~ 1.0 사이에 있는 임의의 값을 float 형태로 반환
numRandom2 = random()
print(numRandom2)

# randrage(start, stop, step) 함수는 start에서 stop까지 step의 값에 따라서 임의의 수를 반환
# numRandom3 = randrange(0, 101, 2)
# print(numRandom3)
#
# if numRandom1 == 1:
#     print("The value of the dice", numRandom1)
# elif numRandom1 == 2:
#     print("The value of the dice", numRandom1)
# elif numRandom1 == 3:
#     print("The value of the dice", numRandom1)
# elif numRandom1 == 4:
#     print("The value of the dice", numRandom1)
# elif numRandom1 == 5:
#     print("The value of the dice", numRandom1)
# else:
#     print("The value of the dice", numRandom1)
#
# numYear = int(input("Your birth year"))
# age = (2022 - numYear) + 1
# print(age)
# if (age > 8) and (age <= 13):
#     print("Elementary school student")
# elif (age > 14) and (age <= 16):
#     print("Middle school student")
# elif (age > 17) and (age <= 19):
#     print("High school student")
# elif (age > 20) and (age <= 27):
#     print("university student")
# else:
#     print("Worker")

# month = int(input("Enter the Month \n "))
#
# if month == 2:
#     print("last day 28")
# elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
#     print("last day 30")
# else:
#     print("last day 31")
#
# year = int(input("Enter the year \n"))
#
# if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
#     print("Leap year")
# else:
#     print("Not leap year")

numRandom1 = randint(1, 100)
print(numRandom1)
count = 0;
while True:
    numUser = int(input("Enter the integer (1~100)"))
    if numUser == numRandom1:
        count += 1
        print("Success count : ", count)
        print("Exit")

        break
    elif numUser > numRandom1:
        count += 1
        print("Big")

    else:
        count += 1
        print("Small")
