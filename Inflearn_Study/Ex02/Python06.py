###############################
# TITLE : Shallow/Deep Copy
# CREATE DATE : 2022-01-29
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import copy
def shallow_copy(list):
    list[2] = 2.5
    print(id(list))

list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(list01)
shallow_copy(list01)
print(list01)
print(id(list01))

list02 = list(list01)

print(id(list01))
print(id(list02))

list03 = copy.deepcopy(list02)
print(id(list03))

list01[1] = 1.5
list02[2] = 2.5
list03[2] = 3.5
print(list01)
print(list02)
print(list03)

index01 = [1, 2, 3, 4, 5, 6, 7, 8]
index02 = index01[:]
print(id(index01))
print(id(index02))

index01[0] = 0.5
print(index01)
print(index02)

def copy_func(x):
    print("x = ", x, "address = ", id(x))
    x+=15
    print("x = ", x, "address = ", id(x))


y = 10
print("y = ", y, "address = ", id(y))
copy_func(y)
print("y = ", y, "address = ", id(y))


def copy_func(x_list):
    print("x = ", x_list, "address = ", id(x_list))
    x_list.append(15)
    print("x = ", x_list, "address = ", id(x_list))


y_list = [1, 2, 3, 4]
print("y = ", y_list, "address = ", id(y_list))
copy_func(y_list)
print("y = ", y_list, "address = ", id(y_list))
