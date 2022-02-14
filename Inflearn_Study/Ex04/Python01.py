###############################
# TITLE : OOP Object-Oriented Programming
# CREATE DATE : 2022-02-14
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

"""
class element
 -member variable(filed, attribute)
 -member method
 -constructor
"""


class Car:

    # field
    color = ""
    name = ""
    speed = 0

    def set_name(self, name):
        self.name = name

    def up_speed(self, speed):
        # self == this
        if speed < 0:
            print("Error")
            return
        self.speed = speed

    def down_speed(self, speed):
        if speed < 0:
            print("Error")
            return
        self.speed = speed

    def change_color(self, color):
        self.color = color

    def print_carInfo(self, name):
        print("Name : {} Speed : {} , Color : {}".format(self.name, self.speed, self.color))


class Television:
    color = ""
    power = False
    channel = 0
    volume = 0

    def set_power(self, power):
        self.power = not power

    def up_channel(self, channel):
        if channel < 0:
            print("Error")
            return
        self.channel = channel

    def down_channel(self, channel):
        if channel < 0:
            print("Error")
            return
        self.channel = channel

    def up_volume(self, volume):
        if volume < 0:
            print("Error")
            return
        self.volume = volume

    def down_volume(self, volume):
        if volume < 0:
            print("Error")
            return
        self.volume = volume

    def __str__(self):
        print(self.color)
        print(self.channel)
        print(self.volume)
        print(self.power)


if __name__ == "__main__":
    # myCar1 = Car()
    # myCar2 = Car()
    # myCar3 = Car()
    #
    # print("myCar1 id :{}, type: {}".format(id(myCar1), type(myCar1)))
    # print("myCar2 id :{}, type: {}".format(id(myCar2), type(myCar2)))
    # print("myCar3 id :{}, type: {}".format(id(myCar3), type(myCar3)))
    #
    # print("=" * 20)
    # myCar1.name = "K7"
    # myCar1.color = "white"
    # myCar1.up_speed(80)
    # myCar1.print_carInfo(myCar1.name)
    #
    # myCar2.name = "GENESIS"
    # myCar2.color = "black"
    # myCar2.up_speed(-120)
    # myCar2.print_carInfo(myCar2.name)

    luckyGold = Television()

    luckyGold.color = "Black"
    luckyGold.volume = 50
    luckyGold.channel = 5
    luckyGold.power = True

    luckyGold.__str__()