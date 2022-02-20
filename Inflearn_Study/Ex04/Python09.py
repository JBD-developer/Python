###############################
# TITLE : overriding
# CREATE DATE : 2022-02-20
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# super
class Disk:
    __capacity = 0
    __rpm = 0

    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm

    def get_capacity(self):
        return self.__capacity

    def get_rpm(self):
        return self.__rpm

    def show_print(self):
        print("Disk Capacity {} Rpm {}".format(str(self.__capacity), str(self.__rpm)))


class HddDisk(Disk):
    __capacity = 0
    __rpm = 0

    def __init__(self, capacity, rpm):
        Disk.__init__(self, capacity, rpm)
        self.__capacity = capacity
        self.__rpm = rpm

    def get_capacity(self):
        return self.__capacity

    def get_rpm(self):
        return self.__rpm

    def show_print(self):
        print("Disk Capacity %s Rpm %s" %( str(self.__capacity), str(self.__rpm)))


class Car:
    value = "Super class"

    def car_method(self):
        print("super class method")


class Sedan(Car):
    value = "Sub class"

    def car_method(self):

        super().car_method()
        print("super class method", super().value)
        print("sub class method", self.value)


if __name__ =="__main__":
    sedan = Sedan()
    sedan.car_method()

    disk = Disk(500, 7200)
    hdd = HddDisk(400, 4500)
    disk.show_print()
    hdd.show_print()

