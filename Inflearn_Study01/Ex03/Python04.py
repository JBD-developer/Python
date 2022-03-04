###############################
# TITLE : data structure
# CREATE DATE : 2022-02-06
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# set
# set_test = {1, 2, 3, 4, 5, 5, 5}
#
# print(set_test)
# print(type(set_test))
# print(len(set_test))
#
# set_test = {"Apple", 3.14, 35, ("a", "b")}
# print(set_test)
#
# for i in set_test :
#     print(i)
# numbers = set()
# print(type(numbers))
# set_test.add(5)
# print(set_test)
# set_test.update([1, 2, 3, 4, 5])
# print(set_test)
#
# set_1 = {1, 2, 3}
# set_2 = {4, 45, 6}
# set_3 = {1, 2, 3, 4, 5, 6 }
# if set_1 == set_2 :
#     print(True)
# else:
#     print(False)
#
# if set_1 < set_3:
#     print(True)
# else:
#     print(False)
#
# print(set_1.issubset(set_2))
# print(set_3.issuperset(set_1))
#
# set_union = set_1.union(set_2)
# print(set_union)
# set_intersection = set_1.intersection(set_3)
# print(set_intersection)
# set_diff = set_3.difference(set_1)
# print(set_diff)

set1 = {2, 1, 34, 5, 3}
print(set1)
set2 = {"Hi", "Hello" , "Human", "Car"}
print(set2)
print(len(set1))
print(len(set2))

set3 = {1, "Hi", "Hello", "Human", "Car", "Car", "Hi", 1, 2}
print(set3)
print(len(set3))

if "Hello1" in set3 :
    print("Hello")
else:
    print("Not")

for i in set3:
    print(i, end=" ")

print("=============")
season = set()
season.add("Spring")
season.add("Summer")
season.add("Fall")
season.add("Winter")
print(season)

print("=============")
# set5 = {1, 1.1, 2, "Car", [10, 20]}
set5 = {1.1, 2, "Car", (10, 20)}
print(set5)

set6 = set()

set6.update(["Human", 1, 34, 5, -10])
print(set6)
set6.clear()
set6.update("Human", [1, 34, 5, -10])
print(set6)

if "H" in set6:
    set6.discard("H")
print(set6)

if 1 in set6:
    set6.remove(1)
print(set6)

SET1 = {10, 20, 30}
SET2 = {10, 20, 30}
print(SET1 == SET2)
print(SET1 != SET2)

SET1 = {10, 20, 30, 40, 50, 60}
SET2 = {10, 20, 30}

print(SET2 <= SET1)
print(SET2.issubset(SET1))
print(SET1.issuperset(SET2))
SET_STRING = set("HELLO")
print(SET_STRING)

if "H" in SET_STRING:
    print("H is included in SET_STRING")


SET1 = {10, 20, 30, 40, 50, 60}
SET2 = {10, 20, 30, 70, 80}
SET3 = set()
SET3= SET1.union(SET2)
print(SET3)
print(SET1 | SET2)

print(SET1.intersection(SET2))
print(SET1 & SET2)

print(SET2 - SET1)
print(SET2.difference(SET1))
print(SET1.difference(SET2))

SET1 = {10, 20, 30, 40, 50, 60}
SET2 = {0, 0, 0, 0, 80}

print(all(SET1))
print(all(SET2))
print(any(SET2))
print(SET1.isdisjoint(SET2))

print(SET1.pop())
print(SET1)

for _ in range(0, len(SET1)):
    # print(SET1.pop())
    print(SET1.discard(10))
print(len(SET1))
print(SET1)

party_1 = set(["Python", "Java", "CSharp", "C", "JavaScript"])
party_2 = set(["TypeScript", "Java", "Ruby", "R"])

print(party_1 & party_2)


def process(word):
    out_word = ""
    for ch in word:
        if ch.isalpha():
            out_word += ch
    return out_word.lower()


if __name__ == "__main__":

    fp = open("E:\\workSpace_Etc\\data.txt", mode="r", encoding="UTF-8")

    set_read = set()
    for line in fp:
        linewords = line.split()
        for word in linewords:
            set_read.add(process(word))

    print(set_read)
    print(len(set_read))

