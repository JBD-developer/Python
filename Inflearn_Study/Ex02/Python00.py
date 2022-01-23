###############################
# TITLE : function
# CREATE DATE : 2022-01-23
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# Ex02. Python01
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


# Ex02. Python02
