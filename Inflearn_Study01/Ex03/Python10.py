###############################
# TITLE : collections module
# CREATE DATE : 2022-02-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# built in data structure
# deque, OrderedDict, defaultdict, counter, namedtuple
from collections import Counter

# counter
text = list("high school")
print(text)
print(type(text))

count = Counter(text)
print(count)
print(count["h"])
# elements()
print(sorted(count.elements()))
print("===========================")

count = Counter({"가":4, "나":3})
print(count)
print(list(count.elements()))
print("===========================")
cnt = Counter(a=2, b=3, c=1, d=4)
print(cnt)
print(type(cnt))
print(len(cnt))
print(sorted(cnt.elements()))
print("===========================")

count = Counter()
print(count)
count.update("Hello")
print(count)
count.update({"H":5})
print(count)
print(list(count.elements()))

print("===========================")

count = Counter("orange, apple ,grape")
print(count.most_common())

print("===========================")
c1 = Counter("Hello Python")
c2 = Counter("Hello")
print(type(c1.subtract(c2)))
print(c1)

# operator

c3 = Counter(["a, b, c, d"])
c4 = Counter("apple")
print(c3)
print(c4)
print("c3 + c4 : {}". format(c3 + c4))
print("c3 - c4 : {}". format(c3 - c4))

print("===========================")

c5 = Counter("abcdef")
c6 = Counter("defghi")
print(c5 & c6)
print(c5 | c6)

# print(c5 * c6)
# print(c5 / c6)


print("===========================")
cnt1 = Counter({"Red":3, "Blue":4})
print(cnt1)
print(list(cnt1.elements()))

print("===========================")
# update()
cnt2 = Counter()
print(cnt2)
cnt2.update("abcdefg")
print(cnt2)

print("===========================")
# most_common()
cnt3 = Counter({"apple", "orange", "grape"})
cnt4 = Counter("apple, orange, grape")
print(cnt3.most_common())
print(cnt4.most_common())

print("===========================")
#subtract
cnt5 = Counter("Life is too short you need python")
cnt6 = Counter("Hello python")
print(cnt5.subtract(cnt6))
print(cnt5)
