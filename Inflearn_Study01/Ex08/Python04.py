###############################
# TITLE : Iterator Generator
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import time
# class MyEnumerate():
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.index >= len(self.data):
#             raise StopIteration
#
#         value = (self.index, self.data[self.index])
#         self.index += 1
#         return value

def infinity_gen():
    num = 0
    while True:
        yield num
        time.sleep(3)
        num += 1
        print("infinity", num)


if __name__ == "__main__":
    # for index, letter in MyEnumerate("abd"):
    #     print(index, ":", letter)
    for i in infinity_gen():
        print("for", i)