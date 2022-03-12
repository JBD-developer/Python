###############################
# TITLE : operator overloading
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

class Figure():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

class Quadrangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __add__(self, other):
        return Quadrangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return "" + str(self.width) + ":" + str(self.height)


if __name__ == "__main__":
    qu1 = Quadrangle(10, 20)
    figure1= Figure(20, 30)
    print(qu1 + figure1)
    print(qu1.width + figure1.width)
