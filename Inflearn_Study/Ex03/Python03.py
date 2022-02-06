###############################
# TITLE : data structure
# CREATE DATE : 2022-02-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-06
# VERSION : 1.0.0
###############################

import math
# tuple

# colors = ("Red", "Orange", "Yellow", "Green", "Blue")
# numbers = (1, 2, 3, 4, 5, 6)
# print(colors)
# print(numbers)
#
# inner_tuple = (1, 2, 3, "Hello")
# outer_tuple = inner_tuple, (4, 5, 6, "Bye")
# print(type(outer_tuple))
#
# tuple_one = (1, 2, 3, 4)
# tuple_two = (5, 6, 7, 8)
# tuple_sum = tuple_one + tuple_two
# print(tuple_sum)
# print("__eq__", tuple_one.__eq__(tuple_two))
#
#
# tuple_1 = (10)
# tuple_2 = (10, )
# print(type(tuple_1))
# print(type(tuple_2))
#
# list_test = [1, 2, 3, 4, 5]
# print(list_test)
# tuple_test = tuple(list_test)
# print(tuple_test)
#
# tuple_3 = (1, 2, 3, 4, 5, 6)
# print(len(tuple_3))
# print(max(tuple_3))
# print(min(tuple_3))
# print(dir(tuple_3))


# tuple packing / unpacking

tuple_test1 = (1, 2, 3, 4)
(a, b) = (100, 200)
print((a, b))
(c, d) = (b, a)
print((c, d))

language = ("Python", 3.8, "Interpreter")
(name, version, type) = language
print("name : " , name, "version : ", version, "type : ", type)


def circle_area():
    radius = float(input("Enter the radius : \n"))
    area = math.pi * radius * radius
    circumstance = 2 * math.pi * radius
    return (area, circumstance)

if __name__ =="__main__":

    tuple_result = circle_area()
    (area,  circumstance) = tuple_result
    print("area", area, "circumstance", circumstance)

    student_list = [(80, 100), (70, 90), (65, 78)]

    for i, score in enumerate(student_list):
        print(i, score)
        sum_score = 0
        for j in range(len(score)):
            sum_score += score[j]
        print("total", sum_score, "avg", sum_score /2.0)
