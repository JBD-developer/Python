###############################
# TITLE : operator overloading
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# str1 = "Hello world"
# str2 = "Life too short you need python"
# print(str1.__add__(str2))
# print(str1 + str2)
# print("="*30)
import math
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("__add__")
        x = self.x + other.x
        y = self.x + other.y
        return Point(x, y)

    def __str__(self):
        print("__str__")
        return "Point" + "(" + str(self.x)+ "," + str(self.y) + ")"

class NumBox():
    def __init__(self, num):
        self.num = num

    def __add__(self, num):
        self.num += num

    def __radd__(self, num):
        self.num += num

    def __sub__(self, num):
        self.num -= num

class Circle():
    def __init__ (self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __str__(self):
        return "Circle radius : " + str(self.radius)



if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print(p1 + p2)

    n = NumBox(40)
    n + 40
    print(n.num)
    n - 20
    print(n.num)
    40 + n
    print(n.num)

    c1 = Circle(5)
    c2 = Circle(7)
    print(c1.get_radius())
    print(c2.get_radius())
    print(c1 > c2)
    c3 = c1 + c2
    print(c3.get_radius())
    print(c1 + c2)