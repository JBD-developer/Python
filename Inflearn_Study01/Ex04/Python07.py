###############################
# TITLE : Inheritance
# CREATE DATE : 2022-02-20
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
class Phone(object):

    def __init__(self):
        self.model = ""
        self.color = ""

    def power_on(self):
        print("Power on")

    def power_off(self):
        print("Power off")

    def ring_bell(self):
        print("The bell rings")

    def send_voice(self, message):
        print("send", message)

    def receive_voice(self, message):
        print("receive", message)


class DMBPhone(Phone):

    def __init__(self, model, color, channel):
        Phone.__init__(self)
        # super.__init__()
        # super.__init__()
        self.model = model
        self.color = color
        self.channel = channel

    def turn_on(self):
        print("Channel : {} start".format(self.channel))

    def turn_off(self):
        print("Channel : {} stop".format(self.channel))

    def change_channel(self, channel):
        self.channel = channel
        print("Change : {} channel".format(self.channel))


class Car:
    speed = 0
    door = 4

    def __init__(self, speed, door):
        self.speed = speed
        self.door = door

    def up_speed(self, value):
        self.speed += value
        print("Current speed super class :%d" %self.speed)

    def __str__(self):
        print(self.speed)
        print(self.door)


class Sedan(Car):

    def __init__(self, speed, door):
        Car.__init__(self, speed, door)
        # self.speed = speed

    def up_speed(self, value):
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
        print("Current speed sub class %d" % self.speed)


class Truck(Car):
    pass


if __name__ == "__main__":
    # car1 = Car(40, 4)
    # car1.up_speed(50)
    # car1.__str__()
    # print("-"*20)
    # car2 = Sedan(50, 3)
    # car2.up_speed(30)
    # print("-"*20)
    # car2.__str__()
    # truck = Car(130, 2)
    # truck.up_speed(20)

    dmb = DMBPhone("chocolate ", "Black", 10)
    print("Model : {}".format(dmb.model))
    print("Color : {}".format(dmb.color))
    print("Channel : {}".format(dmb.channel))

    dmb.power_on()
    dmb.ring_bell()
    dmb.send_voice("Hello")
    dmb.receive_voice("What?")
    dmb.turn_on()
    dmb.change_channel(20)
    dmb.turn_off()
