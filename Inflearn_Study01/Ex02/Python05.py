###############################
# TITLE : list
# CREATE DATE : 2022-01-29
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

marvel_heros = ["Ironman", "Spiderman", "Hulk", "Captainamerica", "Blackpanther"]
dc_heros = ["Superman", "Batman", "Wonderwoman", "Joker", "Joker", "Joker"]

print(marvel_heros)
marvel_heros.append("Ant man")
print(marvel_heros)
marvel_heros.insert(0, "Thor")
print(marvel_heros)

print("Ironman" in marvel_heros)
print("Hawkeye" in marvel_heros)

index = marvel_heros.index("Hulk")
print(index)

if "Hulk" in marvel_heros:
    index = marvel_heros.index("Hulk")
    print("Hulk index : ", index)
else :
    print("It doesn't exist.")

# list.del(index)
# list.pop(index)
# list.remove(name)

print(marvel_heros)
if "Hulk" in marvel_heros:
    print(marvel_heros)
    index = marvel_heros.index("Hulk")
    print("Hulk index : ", index)
    element = marvel_heros.pop(index)
    print(element)
    print("marvel_heros pop hulk :" ,marvel_heros)
else :
    print("It doesn't exist.")


name = "Joker"
while name in dc_heros:
    dc_heros.remove(name)
print(dc_heros)

dc_heros = ["Superman", "Batman", "Wonderwoman", "Joker", "Joker", "Joker"]

print(dc_heros[0])
print(len(dc_heros))
#
# del dc_heros[:]
# print(dc_heros)
# element = dc_heros.clear()
# print(element)
# print(dc_heros)

count1 = dc_heros.count("Joker")
count2 = marvel_heros.count("Ironman")

print(count1)
print(count2)

li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
li3 = ['a', 'b', 'c']
print(li1 + li2)
li1.extend((li3))
print(li1)


li1 = [10, 11, 12]
li2 = [10, 11, 12]

print(li1 == li2)

li3 = [10, 11, 12]
li4 = [10, 11, 13]

print(li3 >= li4)

li5 = ['a', 'b', 'c']
li6 = ['a', 'b', 'd']

print(li5 < li6)

print(ord('c'))
print(ord('d'))

print(chr(100))
print(chr(99))

li7 = ['z', 'x','a', 'c', 'f', 'b']
print("Before sort:" , li7)
li7.sort()
print("After sort:", li7)

li8 = ['100', '2','3', '1', '9', '4']
print("Before sort:", li8)
sorted_li8 = sorted((li8))
print("After sort:", li8)
print(sorted_li8)

print("==============================")
li8 = [1, 100, 5, 2, 11, 8]
li8.sort(reverse=True)
print(li8)

li9 = ["korea","japan", "france", "america", "china", "india"]
sorted_li9 = sorted(li9, key=str.lower)
print(sorted_li9)


li9 = "C#,Python,Java,Ruby,JavaScript"
li10 = li9.split(",")
print(li10)
