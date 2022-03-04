###############################
# TITLE : overriding
# CREATE DATE : 2022-02-20
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
import turtle
import random
class Car:
    speed = 0

    def up_speed(self, speed):
        self.speed += speed
        print("current speed(super class) : % d" % self.speed)

    # private
    def __down_speed(self, speed):
        self.speed -= speed
        print("current speed(super class) : % d" % self.speed)

    def call(self):
        self.__down_speed(100)


class Sedan(Car):

    def up_speed(self, speed):
        self.speed += speed
        if self.speed >=150:
            self.speed = 150
        print("up current speed(sub class) : % d" % self.speed)

    def down_speed(self, speed):
        self.speed -= speed
        print("down current speed(sub class) : % d" % self.speed)


class Truck(Car):
    pass


class Shape:

    myTurtle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTurtle = turtle.Turtle()

    def set_pen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        print("red : {} green :{} blue :{}" .format(r, g, b))

        self.myTurtle.pencolor((r, g, b))
        penSize =random.randrange(1, 20)
        self.myTurtle.pensize(penSize)

    def draw_shape(self):
        pass

class Rectangle(Shape):
    width = 0
    height = 0

    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
        print("Ractangle width : {} height : {}".format(self.width, self.height))

    def draw_shape(self):
        sx1, sy1 = 0, 0
        sx2, sy2 = 0, 0

        sx1 = self.cx - self.width // 2;
        sy1 = self.cy - self.height// 2;

        sx2 = self.cx + self.width // 2;
        sy2 = self.cy + self.height // 2;
        print("sx1 {} sy1 {}".format(sx1, sy1))
        print("sx2 {} sy2 {}".format(sx2, sy2))
        self.set_pen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)

def screen_left_click(x, y):
    rect = Rectangle(x, y)
    rect.draw_shape()


if __name__ == "__main__":
    # sedan = None
    # truck = None
    #
    # sedan = Sedan()
    # truck = Truck()
    # print(sedan.speed)
    # print("=" * 20)
    # sedan.up_speed(100)
    # truck.up_speed(100)
    #
    # sedan.down_speed(120)
    # car = Car()
    # car.call()

    turtle.title("Test")
    turtle.onscreenclick(screen_left_click, 1)
    turtle.done()
