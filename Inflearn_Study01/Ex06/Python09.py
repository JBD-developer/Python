###############################
# TITLE : File try ~ except ~ finally
# CREATE DATE : 2022-03-06
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

(x, y) = (2, 0)

try:
    z = x / y
except ZeroDivisionError:
    print("All numbers cannot be divided by zero.")

try:
    num = int(input("Enter the number"))
except ValueError:
    print("It's not an integer")

"""
try:
    filename = input("Enter the filename")
    with open("Ex06_File\\test10.txt", "r") as data:
        for word in data:
            print(word)
except FileNotFoundError:
    print("The file does not exist")
try:
    filename = input("Enter the filename")
    with open("Ex06_File\\"+filename, "w") as data:
        data.write("enter test")
except FileNotFoundError:
    print("The file does not exist")
else:
    print("Success")
"""
raise NameError("An inaccurate name")
