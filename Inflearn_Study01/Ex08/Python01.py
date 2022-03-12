###############################
# TITLE : Iterator Generator
# CREATE DATE : 2022-03-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

for i in [1, 2, 3, 4]:
    print(i, end=" ")

for s in "Python":
    print(s, end=" ")

print()
"""    
   Iterator
   __iter()__ 
   __next()__ 
"""

class MyCounter(object):

    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

if __name__ == "__main__":

    mycounter = MyCounter(1, 10)
    for n in mycounter:
        print(n, end=" ")