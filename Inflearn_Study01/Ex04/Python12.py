###############################
# TITLE : Polymorphism
# CREATE DATE : 2022-02-24
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-25
# VERSION : 1.0.0
###############################

class Product:
    price = 0
    bonusPoint = 0

    def __init__(self, price):
        self.price = price
        self.bonusPoint = (self.price / 10.0)


class Tv(Product):

    def __init__(self, price):
        super().__init__(price)

    def __str__(self):
        return "TV"


class Computer(Product):

    def __init__(self, price):
        super().__init__(price)

    def __str__(self):
        return "Computer"


class Audio(Product):

    def __init__(self, price):
        super().__init__(price)

    def __str__(self):
        return "Audio"


class Buyer:
    money = 1000
    bonusPoint = 0

    def buy(self, product):
        if self.money < product.price:
            print("Lack of balance")
            return

        self.money -= product.price

        self.bonusPoint += product.bonusPoint
        print(product.__str__())

if __name__ == "__main__":
    buyer = Buyer()
    tv = Tv(300)
    computer = Computer(100)
    audio = Audio(50)

    buyer.buy(tv)

    print("Balance : ", buyer.money)
    print("Bonus point : ", buyer.bonusPoint)
