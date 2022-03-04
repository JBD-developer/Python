###############################
# TITLE : Polymorphism
# CREATE DATE : 2022-02-24
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-25
# VERSION : 1.0.0
###############################
class SalesWorker:

    def __init__(self, name):
        self.__name = name

    def work_info(self):
        print(self.__name, "Sell")


class DeveloperWorker(SalesWorker):

    def __init__(self, name):
        super().__init__(name)
        self.__name = name

    def work_info(self):
        print(self.__name, "Developer")



class Animal:

    def __init__(self, name, age, weight, instance):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__instance = instance

    def show_info(self):
        print("Name :{}".format(self.__name))
        print("Type :{}".format(self.__instance.d_name))
        print("Age :{}".format(self.__age))
        print("Weight :{}".format(self.__weight))
        self.__instance.sound()
        print("=" * 20 )

class Tiger():

    d_name = "Tiger"

    def sound(self):
        print("Tiger : Whoops! Whoops!")


class Dog():

    d_name = "Dog"

    def sound(self):
        print("Dog :  bark! bark!")


class Cat( ):

    d_name = "Cat"

    def sound(self):
        print("Cat :  Meow! Meow!")

if __name__ == "__main__":
    ani1 = Animal("Horang", 8, 180, Tiger())
    ani2 = Animal("Nabi", 4, 8, Cat())
    ani1.show_info()
    ani2.show_info()

    worker1 = SalesWorker("Mike")
    worker2 = SalesWorker("John")
    worker3 = SalesWorker("Anna")

    worker4 = DeveloperWorker("Kane")
    worker5 = DeveloperWorker("Tom")

    worker = [worker1, worker2, worker3, worker4, worker5]

    for info in worker:
        info.work_info()




