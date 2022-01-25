###############################
# TITLE : function
# CREATE DATE : 2022-01-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
import math
from math import *


def list_test01(my_list):
    # my_list = [1, 2, 3, 4]
    my_list += [101, 102]
    print("list_test01 : my_list", my_list)


my_list = [100, 200, 300]
list_test01(my_list)
print(my_list)

# The circumference and area of the circle.
PI = 3.1415892


def main() :
    radius = float(input("circle radius : \n"))
    print("radius :", radius)
    print("circle area : ", circle_area(radius))
    print("circle circumference : ", circle_circumference(radius))

    a, b, c = multi_value()
    print(a, b, c)
    temp_return = multi_value()
    print(type(temp_return))
    li = list(temp_return)
    print(li)
    print(get_sum(11, 18))
    print(total(10, 15))

    # function object
    print((lambda x, y : x + y)(22, 33))
#  3.141592 * (radius ** 2)


def circle_area(i_radius):
    return pow(i_radius, 2) * PI


def circle_circumference(i_radius):
    return 2 * PI * i_radius


def multi_value():
    return  "tuple1", "tuple2", "tuple3"


def get_sum(x, y):
    return x + y


total = lambda x, y : x + y


li = [lambda x: x ** 2, lambda y:y ** 3, lambda x: x ** 4]
main()

for f in li :
    print("labbda :" , f(10))