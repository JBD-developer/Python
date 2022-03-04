###############################
# TITLE : data structure
# CREATE DATE : 2022-02-07
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-02-08
# VERSION : 1.0.0
###############################

# dictionary
# key value
from sympy import trigamma

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

scores = {"Korean":80, "Math":90, "English":80}

print(scores.keys())
print(type(scores.keys()))

# key
for subject in scores:
    print(subject)

for subject in scores.keys():
    print(subject)

print("-------------------")

print(scores.values())
print(type(scores.values()))

for subject in scores.values():
    print(subject)

print("-------------------")
print(scores.items())
print(type(scores.items()))

for subject in scores.items():
    print(subject)

# dictionary comprehension
print("-------------------")
triples = { x:x*x*x for x in  range(6)}
print(type(triples))
print(triples)


# dictionary sort
print("-------------------")
dic1 = {"Pen": 1, "Book": 5, "Bottle": 4, "Coin": 3, "Cup": 2, "Car": 6}
print(dic1)
lst1 = list(dic1)
print(lst1)

lst2 = sorted(dic1)
print(lst2)

lst3 = sorted((dic1.values()))
print(lst3)

print(sorted(dic1, key=dic1.__getitem__))
print(dic1.__getitem__)
print("-------------------")


def dictionary_search():
    eng_dict = dict()
    eng_dict["one"] = "하나"
    eng_dict["two"] = "둘"
    eng_dict["three"] = "셋"
    eng_dict["four"] = "넷"
    eng_dict["five"] ="다섯"


    while True:
        words = input("Enter the word")
        if words == "Exit":
            print("Exit")
            break
        else:
            if words in eng_dict:
                print(eng_dict[words])
            else:
                print("Not")


def dictionary_count():
    word_dict= dict()
    fp = open("E:\\workSpace_Etc\\data.txt", mode="r", encoding="UTF-8")

    for line in fp:
        words = line.split()
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

    print(word_dict)
    fp.close()


if __name__  == "__main__":
    # dictionary_search()
    dictionary_count()

