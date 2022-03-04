###############################
# TITLE : none
# CREATE DATE : 2022-02-19
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
"""
 variable type
    local variable
    global variable
    instance variable
"""

class Bag :
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add2(self, x):
        self.add(x)

    def __str__(self):
        for x in range(len(self.data)):
            print(str(self.data[x]))


class Tv :
    power = False
    channel = 0
    volume = 0

    # def __init__(self, power, channel, volume):
    #     self.power = power
    #     self.channel = channel
    #     self.volume = volume

    def get_power(self):
        self.power = not self.power
        return self.power

    def __str__(self):
        print(self.power)
        print(self.channel)
        print(self.volume)

class Character :
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__hp = Character.NORMAL

    def level_up(self):
        self.__hp = Character.STRONG

    def get_damage(self):
        self.__hp = Character.WEAK

    def __str__(self):
        print("HP :", self.__hp)

if __name__ == "__main__":
    bag1 = Bag()
    bag1.add("Bag1")
    bag1.__str__()
    bag1.add("Bag2")
    bag1.__str__()

    tv1 = None
    print(tv1)
    tv2 = Tv()
    tv2.__str__()
    print(tv2.get_power())

    ch = Character()
    ch.__str__()
