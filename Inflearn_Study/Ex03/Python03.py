###############################
# TITLE : data structure
# CREATE DATE : 2022-02-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################


# tuple

colors = ("Red", "Orange", "Yellow", "Green", "Blue")
numbers = (1, 2, 3, 4, 5, 6)
print(colors)
print(numbers)

inner_tuple = (1, 2, 3, "Hello")
outer_tuple = inner_tuple, (4, 5, 6, "Bye")
print(type(outer_tuple))

tuple_one = (1, 2, 3, 4)
tuple_two = (5, 6, 7, 8)
tuple_sum = tuple_one + tuple_two
print(tuple_sum)
print("__eq__", tuple_one.__eq__(tuple_two))


tuple_1 = (10)
tuple_2 = (10, )
print(type(tuple_1))
print(type(tuple_2))

list_test = [1, 2, 3, 4, 5]
print(list_test)
tuple_test = tuple(list_test)
print(tuple_test)

tuple_3 = (1, 2, 3, 4, 5, 6)
print(len(tuple_3))
print(max(tuple_3))
print(min(tuple_3))
print(dir(tuple_3))