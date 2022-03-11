###############################
# TITLE : Sort Search
# CREATE DATE : 2022-03-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# sort sorted


list1 = [4, 2, 1, 5, 7, -1]
list2 = sorted(list1, reverse=True)
print(list1)
print(list2)
print(list1.sort())
print(list1)

print("="*30)

print(sorted({3:"0",2:"B", 5:"B",4:"E", 1:"A"}))
print(sorted("Life is too short you need python".split(), key=str.lower))

print("="*30)

list3 = [
    ("Python", 3.8, 20210111),
    ("Java", 1.8, 20220110),
    ("CPlus", 4.5, 20220311)
]

# ascending descending
print(sorted(list3, key=lambda list3:list3[2], reverse=True))

print("="*30)

data = [(1, 100), (1, 200), (3, 150), (2, 100), (3, 200)]
print(sorted(data, key=lambda data:data[0]))


