###############################
# TITLE : collections module
# CREATE DATE : 2022-02-13
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# built in data structure
# deque, OrderedDict, defaultdict, counter, namedtuple
from collections import namedtuple

# namedtuple

language1 = ("Python", "3.8", "Interpreter")
language2 = ("Java", "1.8", "Interpreter/Compiler")

for n in [language1, language2]:
    print("Name: %s Version: %s Type: %s" %n)

print("Name: %s Version: %s Type: %s" %(language1[0], language1[1], language1[2]))

print("="*20)

Person = namedtuple(typename="Person", field_names=("name age address"))
p1 = Person(name="Mike", age=32, address="Seoul")
p2 = Person(name="Kim", age=28, address="Busan")

for n in [p1, p2]:
    print("Name: %s Age: %s Address: %s" %n)

print(p1.name)
print(p1.age)
print(p1.address)
print(id(p1))

print("="*20)

p3 = Person._make(["Kane", 15, "Daegu"])
print(p3)

print("="*20)

p3 = p3._replace(name="Chan")
p3 = p3._replace(address="Tokyo")
print(p3._fields)
print(p3.__getattribute__("name"))
print(getattr(p1, "name"))
print(getattr(p2, "name"))
print(getattr(p3, "name"))

dic = {"name":"Kim", "age":25, "address":"busan"}
print(dic)
print(type(dic))

p4 = Person(**dic)
print(p4)
print(p4.name, p4.age, p4.address)
print(type(p4))
