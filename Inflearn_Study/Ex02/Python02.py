###############################
# TITLE : function
# CREATE DATE : 2022-01-24
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# call by value (pass by value) - immutable object

def change_value(num):
    num = num + 1
    print(num)


n = 100
print("Before :" + str(id(n)))
change_value(n)
print("After : " + str(id(n)))

msg = "Happy Birthday"
print(id(msg))

msg += "For You"
print(id(msg))

# call by reference - mutable object

def change_reference(li):
    print("Before",li)
    print("Before ID address", id(li))
    li += [100, 200]


list = ["Hello", 1, 2, 3, 4, 5, 1, 1.1]
print("Before :", list)
print("Before address :", id(list))
change_reference(list)
print("============================")
print("After :", list)
print("After address :", id(list))

# dictionary key, value

def change_dic(dic):
    dic["Weight"] = 80

dic = {"Name":"Mike", "Age":39}
print(dic)
print(type(dic))
change_dic(dic)
print(dic["Name"])
print(dic["Age"])
print(dic["Weight"])
print(dic)

# local variable scope
# global variable scope







