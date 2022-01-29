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

del dc_heros[:]
print(dc_heros)
element = dc_heros.clear()
print(element)
print(dc_heros)