###############################
# TITLE : Abstract
# CREATE DATE : 2022-02-26
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
from abc import *


class Unit(metaclass=ABCMeta):
    x = 0
    y = 0
    name = ""

    @abstractmethod
    def move_unit(self, x, y):
        pass

    def stop_unit(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
        print("{}\'s current location {}:{}".format(self.name, self.x, self.y))

class Tank(Unit):
    mode = ""
    # def __init__(self, name):
    #     self.name = name

    def move_unit(self, x, y):
        self.x = x
        self.y = y
        print("{}\'s location {}:{}".format(self.mode, self.x, self.y))

    def type_change(self):
        self.mode = "Attack Mode"
        print("mode change {}".format(self.mode))


class DropShip(Unit):
    mode = ""

    # def __init__(self, name):
    #     self.name = name

    def move_unit(self, x, y):
        self.x = x
        self.y = y
        print("{}\'s location {}:{}".format(self.mode, self.x, self.y))

    def load_mode(self):
        self.mode = "Boarding Mode"
        print("Boarding mode {}".format(self.mode))


class Marine(Unit):
    mode = ""

    # def __init__(self, name):
    #     self.name = name

    def move_unit(self, x, y):
        self.x = x
        self.y = y
        print("{}\'s location {}:{}".format(self.mode, self.x, self.y))

    def stimPack_mode(self):
        self.mode = "StimPack Mode"
        print("StimPack mode {}".format(self.mode))


if __name__ == "__main__":
    print("=" * 20)
    tank = Tank()
    tank.move_unit(100, 300)
    tank.type_change()
    tank.stop_unit("tank", 200, 300)
    print("=" * 20)
    marine = Marine()
    marine.move_unit(200, 300)
    marine.stimPack_mode()
    marine.stop_unit("marine", 300, 400)