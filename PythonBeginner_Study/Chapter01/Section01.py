###############################
# TITLE : Calculator
# CREATE DATE : 2022-02-15
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

def add_num(a, b):
    result = a + b
    print("{} + {} = {}".format(a, b, result))


def sub_num(a, b):
    result = a - b
    print("{} - {} = {}".format(a, b, result))


def mul_num(a, b):
    result = a * b
    print("{} * {} = {}".format(a, b, result))


def div_num(a, b):
    result = a / b
    print("{} * {} = {}".format(a, b, result))

if __name__ == "__main__":
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    add_num(num1, num2)
    sub_num(num1, num2)
    mul_num(num1, num2)
    div_num(num1, num2)