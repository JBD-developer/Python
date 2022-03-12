###############################
# TITLE : Iterator Generator
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
import time
"""
def my_counter(low, high):
    while low <= high :
        yield low
        low += 1


if __name__ == "__main__":
    for n in my_counter(1, 10):
        print(n)


def gen(count):
    start = 1
    while start <= count:
        yield start
        time.sleep(2)
        print("start value", start)
        start += 1

if __name__ == "__main__":
    for i in gen(3):
        print("for", i, end= " ")


def gen():
    list1 = [10, 20, 30]
    yield from list1
    time.sleep(2)
    print("list1 value ", list1)

if __name__ == "__main__":
    test_gen = gen()
    n = next(test_gen)
    print("main n value ", n)
    n = next(test_gen)
    print("main n value ", n)
    n = next(test_gen)
    print("main n value ", n)
"""

class Fiboiterator():
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue

    def __iter__(self):
        return self

    def __next__(self):
        n = self.a + self.b

        if n > self.maxValue:
            raise StopIteration

        self.a = self.b
        self.b = n
        return n

if __name__ == "__main__":

    for i in Fiboiterator():
        print(i)
