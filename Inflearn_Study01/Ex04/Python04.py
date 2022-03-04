###############################
# TITLE : Instance variable class variable
# CREATE DATE : 2022-02-18
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# Instance variable class variable
class Rectangle:

    def __init__(self, side = 0):
        self.side = side

    def get_area(self):
        return self.side * self.side


def print_area(rectangle, count):
    while count >= 1:
        print(rectangle.side, "\t", rectangle.get_area())
        rectangle.side += 1
        count -= 1

class Circle :

    def __init__(self, radius = 0):
        self.radius = radius

    def __eq__(self, other):
        print("__eq__method call")
        return self.radius == other.radius

class Card:
    kind = ""
    number = 0
    width = 40
    height = 100

    def __init__(self, kind, number):
        self.kind = kind
        self.number = number

    def __str__(self):
        print("Card kind {}".format(self.kind))
        print("Card number {}".format(self.number))
        print("Card Width {}".format(Card.width))
        print("Card Height {}".format(Card.height))


class Car:
    color = "" # instance variable
    speed = 0 # instance variable
    count = 0 # class variable

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        Car.count  += 1

    def __str__(self):
        print(self.color)
        print(self.speed)
        print(self.count)

if __name__ == "__main__":
    # print(Car.count)
    # print(id(Car.count))
    # print("="*20)
    # car1 = Car("Red", 120)
    # car1.__str__()
    # print(id(car1.count))
    # print(id(Car.count))
    # print("="*20)
    # car2 = Car("Blace", 140)
    # car2.__str__()
    # print(id(car2.count))
    # print(id(Car.count))

    # card1 = Card("Diamond", 9)
    # card2 = Card("Heart", 8)
    # card1.__str__()
    # card2.__str__()
    rectangle = Rectangle()
    cnt = 5
    print_area(rectangle, cnt)
    print("Rectangle ", rectangle.side)

    cir1 = Circle(10)
    cir2 = Circle(10)

    if cir1 == cir2:
        print("The radius is the same")
