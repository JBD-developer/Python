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


def local_variable1():
    txt = "Python local variable"
    print(txt)


local_variable1()


def local_variable2():
    txt = "Python local variable"
    print(txt)


local_variable1()


# global variable scope


def global_variable():
    print(txt)


txt = "Python global variable"
global_variable()


def global_variable2():
    txt2 = "Python local variable "
    print(txt2)


txt2 = "Python global variable"
global_variable2()


def global_variable3():
    print(txt3)
    # txt3 = "Python study"
    print(txt3)


txt3 = "Java study"
global_variable3()



def global_variable4():
    global txt4
    print(txt4)
    txt4 = "Python study" # global variable  change
    print(txt4)


txt4 = "global variable change"
global_variable4()
print(txt4)


def global_variable5(n1, n2):
    global a
    a = 20
    n1, n2 = n2, n1
    b = 5
    print(a, b, n1, n2)


a = 1
b = 4
n1 = 2
n2 = 3

print(a, b, n1, n2)
global_variable5(n1, n2)


# parameter = local variable


