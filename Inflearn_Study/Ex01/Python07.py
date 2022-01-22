###############################
# TITLE : Iteration
# CREATE DATE : 2022-01-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-01-22
# VERSION : 1.0.0
###############################
import turtle
from math import *
from random import *
from operator import eq
# for x in range(10):
#     print("Hello Python")
#
# for name in ["BUSAN", "SEOUL", "DAEJEOM", "ULSAN", "DAEGUE"]:
#     print("City name :", name )
#
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(x, end=",\t")
#
# sum = 0
# for x in range(10):
#     print(x)
#     sum += x
# print(sum)
#
# for char in "abcdefghi":
#     print(char, end=",")
#
# for x in range(6):
#     print("------------")
#     print("Hello Python")
#
# print(type(range(5)))
# print(range(5))
#
# # range function
# for x in range(1, 11):
#     print(x)
#
# for x in range(1, 11, 3):
#     print(x)
#
# title= "Code name is javaKiller"
#
# for char in title:
#     print(char, end="\t")
# print()
# for char in title:
#     print(char, end="")
#
# numX = int(input("Enter the integer\n"))
# total1 = 0
# for x in range(1, numX + 1):
#     total1 += x
# print(total1)
#
# total2 = 0
# for x in range(101):
#
#     if total2 >= 2000:
#         print(x)
#         break
#     total2 += x
#
#
# # Factorial
# fact = 1.0
# numY = int(input("Enter the integer\n"))
# for i in range(1 ,numY+1):
#     fact *= i
# print (numY, "Factorial :", fact)
#
# # Fibonacci
# n1 = 1
# n2 = 1
# n3 = 1
#
# fibonacci = int(input("Enmter the Fibonacci \n" ))
# for i in range(1, fibonacci):
#     if i < 3:
#         n3 = 1
#     else :
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#
#     if n3 < fibonacci:
#         print(n3, end=",")
#
# # C = (F - 32) * 5 / 9
#
# for t in range(0, 101, 10):
#     c = (t - 32) * 5.0 / 9.0
#     print(t, ":\t ", round(c, 2))
#
#
# # multiplication table
#
# for i in range(1, 10):
#     print(2,  "*", i, "=",(2 * i))
#
# for i in range (2, 10):
#     for j in range (1, 10):
#         print(i, "*",j, "=", (i*j))
#
#
# numX = int(input("Enter the integer\n"))
# numY = int(input("Enter the integer\n"))
# count = 0 ;
# for i in range(numX, numY+1):
#     if (i % 3 == 0) and (i % 4 == 0):
#         continue
#     count += 1
#     print(count, "count :" , i)
#
#
# p = turtle.Pen()
#
# for i in range(50):
#     p.forward(50)
#     p.right(144)
#
# for i in range(10):
#     p.left(20)
#
#     p.forward(50)
#     p.left(90)
#     p.forward(50)
#     p.left(90)
#     p.forward(50)
#     p.left(90)
#     p.forward(50)
#     p.left(90)
#     p.forward(50)
#     p.left(90)
#     p.forward(50)
#     p.left(90)
#
#
# turtle.exitonclick()

# while
i = 0
while i < 5:
    print("code name is java killer")
    i += 1
print("Exit")

i = 0
while i < 10:
    print(i , end=",")
    i += 1
print("Exit")

sum = 0
i = 0
while i <= 10:
    sum += i
    i += 1
print("Exit")
print("Sum : ", sum)

# Factorial while
i = 1
factorial = 1
while i < 10 :
    factorial *= i
    i += 1
print("5! value %d" % factorial)

print("------------------------------")
i = 1
while i < 10:
    # print(3, "*", i, "=", (3*i))
    # print("3 * %d = %d" % (i,  3*i))
    print("3 * %d = %2d" % (i, 3 * i))
    i += 1

print("------------------------------")
i = 1
sum = 0
while i <= 100:
    if (i % 3) == 0:
        sum += i
    i += 1
print(sum)

print("------------------------------")
num = 1234
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10
print(total)

print("------------------------------")
# sentinel

# numX = int(input("Enter the number of score \n : "))
# numTotal = 0
# numAverage = 0
# count = 1;
# numOriginal = numX
# while numX > 0 :
#     numScore = int(input("Enter the score \n : " ))
#     numTotal += numScore
#     numX -= 1
#     print(numTotal)
#     print("count", count)
#
#     if numOriginal == count:
#         numAverage = numTotal // numOriginal
#         print(numAverage)
#         print(numTotal)
#     count += 1

# cnt = 0
# hap = 0
# score = 0
# aver = 0.0
# print("Please enter a negative number to end the show")
# print("------------------------------")
# while score >= 0:
#     score = int(input(str(cnt + 1) + "Please enter the grades of the next student."))
#
#     if score >= 0:
#         hap += score
#         cnt += 1
#
# if cnt > 0:
#     aver = hap / cnt
#
# print(str(cnt) + " average student is %.1f" %  aver)

# print("------------------------------")

# numX = randint(1, 100)
# print ("Rnadom number : %d" % numX)
#
# cnt = 0
#
# while cnt < 10:
#     numGuess = int(input(str(cnt + 1) + " Enter the number"))
#     cnt += 1
#     if numGuess < numX:
#         print("Small")
#     elif numGuess > numX:
#         print("Big")
#     elif numGuess == numX:
#         print("%d Success %d" % (cnt, numGuess))
#         msg = input("Would you like to go on? Y : N \n")
#         if msg == "N":
#             print("Exit")
#             break
#         else:
#             print("Restart")
#             numX = randint(1, 100)
#             print ("Random number", numX)
#             cnt = 0
#
# print("Fail Exit")
# numTotal = 0
# numPrice = 0
# while True:
#     numPrice = input("Enter the price. If you enter \'Exit\', it's over.")
#     #if numPrice.eq("Exit"):
#     if eq(numPrice, "Exit"):
#     # if numPrice == "Exit":
#         print("Total Price :" + str(numTotal) + "Won")
#         print("Exit")
#         break
#     numTotal += int(numPrice)
#
# numSpeed = 0
# bRun = True
# Keycode = 0
# while bRun:
#     Keycode = int(input("Select : 1: Increase 2 : Decrease 3: Stop "))
#     if Keycode == 1:
#         numSpeed += 10
#         print("Increase current \n speed %d:" % numSpeed)
#     elif Keycode == 2:
#         numSpeed -= 10
#         if numSpeed < 0:
#             print("Speed is not negative number")
#             numSpeed = 0
#         else:
#             print("Decrease current \n speed %d:" % numSpeed)
#     elif Keycode == 3:
#         bRun = False
#         print("Stop current speed %d" % numSpeed )
#         break
#     else :
#         print("Error")
#

# Nested loop
for x in range(5):
    for y in range(10):
        print("*", end="")
    print("")

for x in range(1, 6):
    for y in range(1, 6):
        if y <= x :
            print("*", end="")
    print("")

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("")

print("Integer value : {} , string {} , float {}".format(10, "Ten", 10.0))
print("Integer value : {0} , string {1} , float {2}".format(10, "Ten", 10.0))
print("Integer '{:>5d}'".format(300))
print("Integer '{:<5d}'".format(400))

#
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(6, 0 , -1):
    print("{:<5}".format("*" * (i-1)))

for i in range(1, 6):
    for j in range (5 - i):
        print(" ", end ="")
    for j in range (1, i*2):
        print("*", end="")
    print("")

for i in range(1, 11, 2):
    print("{:^10}".format("*" * i))

for i in range(5):
    for j in range (i):
        print(" ", end="")
    for j in range(10, (i*2) + 1, -1):
        print("*", end ="")
    print("")

numLast = 0
numTotal = 0

for i in range(2, 2001):
    for j in range (2, i+1):
        if i % j == 0:
            break
    if i == j :
        print("prime :" , j)
        numTotal += j
        print("total", numTotal)
