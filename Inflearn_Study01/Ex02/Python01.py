###############################
# TITLE : function
# CREATE DATE : 2022-01-23
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from Python00 import *
import Python00
# def LF_say(name):
#     for i in range(1, 5):
#         print("Hello", name)

# LF_say("CSharp", "codename is java killer")
# LF_say("Java", "JVM")
# LF_say2("Python", "Hi")

Python00.lf_say("CSharp", "codename is java killer")
Python00.lf_say("Java", "JVM")
Python00.lf_say2("Python", "Hi")

result = Python00.calc_get_sum(1, 10)
print(result)

numX = int(input("Enter the integer : \n"))
result = Python00.calc_get_square(numX)
print(result)

result = Python00.calc_get_max_compare(1, 4)
print(result)

result = Python00.calc_get_square2(2, 4)
print(result)

numT = float(input("Enter the temperature : \n"))
result = Python00.fahrenheit_to_celsius(numT)
print(numT , result)

print(check_prime(13))


message = "Y"
result = 0
while True:
    if message == "N":
        break
    elif message == "Y":
        numA = float(input("Enter the first number\n:"))
        numB = float(input("Enter the second number \n"))
        op = input("Enter the  operator [+, - , * , N/] \n")
        if op == "+":
            result = Python00.calc_add(numA, numB)
            print("%f + %f = %f" % (numA, numB, round(result, 2)))
        elif op == "-":
            result = Python00.calc_sub(numA, numB)
            print("%f - %f = %f" % (numA, numB, round(result, 2)))
        elif op == "*":
            result = Python00.calc_mul(numA, numB)
            print("%f * %f = %f" % (numA, numB, round(result, 2)))
        elif op == "/":
            result = Python00.calc_div(numA, numB)
            print("%f / %f = %f" % (numA, numB, round(result, 2)))
        else:
            print("Error")
    else:
        print("Error")
    message = input("Continue? Y:N")
print("Exit")

Python00.print_info("Python", 2)

# default argument

Python00.print_info02("Python")
Python00.print_info02("Python", "Good bye")
Python00.print_info03("Python", 4.8, "Seoul")
Python00.print_info03(address="Python", age=4.8, name="Seoul")

radius = float(input("Enter the radius\n"))
sphere = Python00.sphere_volume(radius)
print("Volume of a sphere : %f" % sphere)

print(Python00.create_password2())

print(Python00.decimal_to_binary2(10))
print(bin(10))
print(oct(10))
print(hex(10))
print("------------------------------")
print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))