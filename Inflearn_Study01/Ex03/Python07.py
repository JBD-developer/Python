###############################
# TITLE : collections module
# CREATE DATE : 2022-02-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# built in data structure
# deque, OrderedDict, defaultdict, counter, namedtuple

from collections import deque
import time
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

# deque
deque_list = deque()

for i in range(5):
    deque_list.append(i)
    print(deque_list)
print(type(deque_list))
print(deque_list.popleft())

# deque appendleft()
print("============")
deque_list2 = deque()
for i in range(5):
    if i % 2 == 0:
        deque_list2.appendleft(i)
    else:
        deque_list2.append(i)
    print(deque_list2)

# deque rotate()
print("============")
deque_list2.rotate(-2)
print(deque_list2)

# deque reversed()
print("============")
deque_list3 = deque()
for i in range(1, 15, 3):
    deque_list3.appendleft(i)
    print(deque_list3)
print(deque(reversed(deque_list3)))

# deque extend() right
print("============")
print(deque_list3)
deque_list3.extend([5, 6, 7])
print(deque_list3)

# deque extendleft() left
print("============")
print(deque_list3)
deque_list3.extendleft([8, 9, 10])
print(deque_list3)

# deque maxlen
print("============")
deque_list3.clear()
print(deque_list3)
basedata_list = ['a', 'b', 'c', 'd', 'e']
deque_list3 = deque(basedata_list, maxlen=4)
print(deque_list3)
print(deque_list3.popleft())
print(deque_list3)

# compare the performance of deque and list
print("============")
deque_list5 =deque()
start_time = time.time()
for i in range(10000000):
    deque_list5.append(i)
end_time = time.time()
print("deque append time: ", end_time-start_time)

list = list()
start_time = time.time()
for i in range(1000000):
    list.append(i)
end_time = time.time()
print("list append time: ", end_time-start_time)

print("============")

start_time = time.time()
for i in range(len(deque_list5)):
    deque_list5.pop()
end_time = time.time()
print("deque pop time: ", end_time-start_time)

start_time = time.time()
for i in range(len(list)):
    list.pop()
end_time = time.time()
print("list pop time: ", end_time-start_time)
