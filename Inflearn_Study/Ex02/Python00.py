###############################
# TITLE : function
# CREATE DATE : 2022-01-23
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-01-28
# VERSION : 1.0.0
###############################

# Ex02. Python01
import math
import random
def lf_say(name, message):
    for i in range(1, 5):
        print("Hello", name, message)


def lf_say2(name, message):
    for i in range(1, 5):
        print(name, message+ "!")


# A function that determines the sum of x to y
def calc_get_sum (x, y):
    total = 0
    for i in range(x, y + 1):
        total += i
    return total


# A function to find the square root
def calc_get_square(x):
    temp = (x ** 2)
    return temp


# A function that seeks repetition square
def calc_get_square2(x, y):
    temp = 1
    for i in range(y):
        temp *=x
    return temp


# A function that compares two numbers to obtain a larger value
def calc_get_max_compare(x, y):
    temp = 0
    if x > y:
        temp = x
    else:
        temp = y
    return temp


def fahrenheit_to_celsius(x):
    temp = (5.0 * (x - 32.0))/9.0
    return round(temp, 2)


def check_prime(x):
    temp = True
    for i in range(2, x):
        if (x % i) == 0:
            temp = False
        else:
            temp = True
        return temp


def calc_add(x, y):
    return x + y


def calc_sub(x, y):
    return x - y


def calc_div(x, y):
    return round((x / y), 2)


def calc_mul(x, y):
    return x * y


def print_info(name, age):
    print("------------")
    print("Name %s" % name)
    print("Age %s" % age )
    print("------------")
    return


def print_info02(name, message = "Hi"):
    print("Hello" + name + "," + message)
    return


def print_info03(name, age, address):
    print("------------")
    print("Name %s" % name)
    print("Age %s" % age)
    print("Address %s" % address)
    print("------------")


def sphere_volume(x):
    result = (4 / 3) * math.pi * math.pow(x, 3)
    return result


def create_password1():
    num_str = "0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(num_str))
        password = password + num_str[index]
    return password


def create_password2():
    password = ""

    for i in range(6):
        index = random.randrange(0 ,9)
        password = password + str(index)
    return password


def decimal_to_binary(x):
    binary = ""
    reminder = 0


def decimal_to_binary2(x):
    binary = ""
    while x != 0:
        value = x % 2
        if value == 0:
            binary = "0" +binary
        else :
            binary = "1" +binary

        x = x // 2
        print("num : ", x)
    return binary


# Ex02. Python02
# Ex02. Python03

def fib(n):
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    while n3 < n:
        print(n3, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3


def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def grade_read_list():
    scorelist = []
    flag = True

    while flag:
        score = int(input("Enter the score:\n"));
        if score < 0 :
            flag = False
            print("Loop exit")
            break;
        else :
            scorelist.append(score)

    return scorelist


def grade_sort_list(list):
    list.sort()
    return list


def grade_print_list(list):
    j = 0
    for i in list:
        print((j+1),":", i)
        j+=1
