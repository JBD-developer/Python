###############################
# TITLE : data structure
# CREATE DATE : 2022-02-07
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# dictionary
# key value

dic = {1: 'apple', 2: "banana"}
print(type(dic))
print(len(dic))

contact = {"Kim":"010-1111-2222","Park":"010-2222-3333", "Jeong":"010-4444-5555"}
print(contact)

print(contact["Kim"])
contact["Choi"] = "010-5555-6666"
print(contact)

print(contact.pop("Choi"))
print(contact)

scores = {"Math" : 90, "Korean":100, "English":70}

for item in scores.items():
    print(item)

for item in scores:
    print(item)

squares = {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25 }
print(1 in squares)


triples = { x: x*x*x for x in range(7)}
print(triples)

print(sorted(scores))
print(sorted(scores.values()))

dic1 = {1 : "Apple", 2 : "Banana", 3 : "Tomato", 4: "Orange"}
print(dic1)

dic2 = {1: "Apple", 2: "Banana", 3: "Tomato", 4: "Orange"}

print(dic2[1])
print(dic2[2])
print(dic2[3])

print(dic.get(1))

a = dic2.get(5, "Peach")
print(a)


dic4 = {1: "Apple", 2: "Banana", 3: "Tomato", 4: "Orange"}

print(id(dic4))
dic4[5] = "Peach"
print(dic4)
print(id(dic4))

print(dic4.pop(5))
print(dic4)
del dic4[4]
print(dic4)

dic4.clear()
print(dic4)