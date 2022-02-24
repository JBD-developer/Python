###############################
# TITLE : multiple inheritance - Method Resolution Order
# CREATE DATE : 2022-02-20
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-24
# VERSION : 1.0.0
###############################

# class University:
#     def __init__(self):
#         pass
#
#     def manage_credit(self):
#         print("Point")
#
#
# class Undergraduate(Person, University):
#     def __init__(self):
#         Person.__init__(self)
#         University.__init__(self)
#
#     def study(self):
#         print("Study");

class Person:
    def __init__(self):
        print("I am human")

    def greeting(self):
        print("Person class greeting")


class Student(Person):

    def __init__(self):
        Person.__init__(self)
        print("I am student")

    def greeting(self):
        print("Student class greeting")


class Worker(Person):

    def __init__(self):
        Person.__init__(self)
        print("I am worker")

    def greeting(self):
        print("Worker class greeting")

# Diamond inheritance
class PartTimer(Student, Worker):

    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("I am PartTimer")

    # def greeting(self):
    #     print("PartTimer class greeting")

if __name__ == "__main__":

    # student = Undergraduate()
    # student.greeting()
    # student.manage_credit()
    # student.study()

    partTimer = PartTimer()
    partTimer.greeting()
    # MRO - Method Resolution Order
    print(PartTimer.__mro__)
