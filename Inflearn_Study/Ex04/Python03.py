###############################
# TITLE : OOP Object-Oriented Programming constructor
# CREATE DATE : 2022-02-17
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-18
# VERSION : 1.0.0
###############################

"""
class element
 -member variable(filed, attribute)
 -member method
 -constructor
"""
from networkx import radius


class Moniter :
    # field
    __company = ""
    __inch = 0
    __price = 0


    def __init__(self, company, inch, price):
        self.__company = company
        self.__inch = inch
        self.__price = price

    def __str__(self):
        print(self.__company)
        print(self.__inch)
        print(self.__price)

    def get_company(self):
        return self.__company

    def get_inch(self):
        return self.__inch

    def get_price(self):
        return self.__price

    def set_company(self, company):
        self.__company = company

    def set_inch(self, inch):
        self.__inch = inch

    def set_price(self, price):
        self.__price = price



class Person:
    __name = "" # private
    age = 0     # pulbic
    address = ""

    def __init__(self):
        self.__name = "Kane"
        self.age = 35
        self.address = "Busan"

    # def __init__(self, name, age, address):
    #     self.name = "Mike"
    #     self.age = age
    #     self.address = address

    def getName(self):
        return self.__name

    def getAge(self):
        return self.age

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.age = age

    def setAddress(self, addesss):
        self.address = addesss

    def __str__(self):
        print(self.__name)
        print(self.age)
        print(self.address)

import math


class Cicle:
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def circle_area(self):
        area = self.__radius * self.__radius * math.pi
        return area

    def circle_circumference(self):
        circum = self.__radius * 2 * math.pi
        return circum

    def __str__(self):
        print("Radius : {}", format(self.radius))

class BankAccount:
    __balance = 0

    def get_balance(self):
        return self.__balance

    def set_deposit(self, mount):
        self.__balance += mount

    def set_withdraw(self, mount):
        if self.__balance < mount:
            print("Error")
        else:
            self.__balance -= mount

    def __str__(self):
        print(self.__balance)

if __name__ == "__main__":
    # person1 = Person()
    # person1.__str__()
    #
    # person2 = Person()
    # person2.__str__()
    # print(person1.getName())
    # print(person2.getAddress())

    moniter1 = Moniter("Sony", 28, 1200000)
    moniter2 = Moniter("Apple", 32, 4000000)
    # moniter1.__str__()
    # moniter2.__str__()
    moniter1.__str__()
    print("=" * 20)
    print(moniter1.get_company())
    moniter1.set_company("Blackberry")
    moniter1.set_price(15000000)
    print("="*20)
    moniter1.__str__()
    print("="*20)


    circle = Cicle(10)
    print(circle.get_radius())
    print(circle.circle_circumference())
    print(circle.circle_area())

    print("=" * 20)
    myaccount = BankAccount()
    myaccount.set_deposit(100000)
    myaccount.__str__()
    myaccount.set_withdraw(1000)
    myaccount.__str__()