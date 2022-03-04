###############################
# TITLE : Special method
# CREATE DATE : 2022-02-19
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# Special method
class Book :

    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def __str__(self):
        return "Title %s \n Author %s \n Page %d" %(self.title, self.author, self.page)

    def len(self):
        return self.page

class Vector2D :

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        add_vector =  Vector2D(self.x + other.x, self.y + other.y)
        return add_vector

    def __sub__(self, other):
        sub_vector = Vector2D(self.x - other.x, self.y - other.y)
        return sub_vector

    def __mul__(self, other):
        mul_vector = Vector2D(self.x * other.x, self.x * other.y)
        return mul_vector

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "(%g, %g)" %(self.x, self.y)
        print("x : {}".self.x)
        print("y : {}".self.y)


if __name__ == "__main__":
    vector1 = Vector2D(5, 2)
    vector2 = Vector2D(5, 3)
    vector3 = Vector2D(5, 4)
    vector_result = vector1 + vector2
    print(vector_result)

    if vector1 == vector2:
        print("the same object")
    else:
        print("not the same object")

    book1 = Book("Python", "Lion", 320)
    print(book1)
    print(book1.len())