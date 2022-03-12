###############################
# TITLE : Module
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# module
import fibo as fb
import copy
import random
import sys
import time
import calendar

from fibo import *
from fibo import fib1
from fibo import fib2

fb.fib1(10)
result = fb.fib2(40)
print(result)

# DeepCopy, ShallowCopy
list1 = [1, 2, 3, 4, 5, 6]
list2 = list1.copy()
list3 = copy.deepcopy(list2)
print(list1)
print(list2)
print("="*30)
list1[0] = 2
list2[3] = 8
print(list1)
print(list2)
print(list3)

num = random.randint(1, 12) # integer
num = random.random() # float
num = random.randrange(0, 100, 3)
print(num)

list1 = ["Python", "Java", "C", "R", "JavaScript", "CSharp"]
print(random.choice(list1))

list2 = [x for x in range(10)]

print("Before", list2)
random.shuffle(list2)
print("After", list2)

print(sys.version)
print(sys.path)
print(sys.prefix)

print(time.time()) # from 1970-01-01
print(time.asctime())

cal = calendar.month(2016, 8)
print(cal)

word = ["Python", "Ruby", "Java", "JavaScript", "C", "R", "SQL", "HTML"]

result = ""

for i in range(0, 3):
    result += random.choice(word)
print(result)

alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, 10):
    letter = random.choice(alpha)
    print(letter)

numX = random.sample([i for i in range(100, 200) if i % 2 == 0 ], 5)
print(numX)