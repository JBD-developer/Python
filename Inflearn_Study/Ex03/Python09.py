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
from collections import defaultdict

# defalutdict

# empty dictionary
# dic = dict()
# print(dic["first"])

dic = defaultdict(lambda:0)
print(dic["first"])
print(dic["second"])
print(dic[10])
print(dic.get('first'))
print(dic)

print("int=============")

dic = defaultdict(int)
print(dic["a"])
print(dic.get("a"))
print(type(dic))
print(dic)

print("float=============")

dic = defaultdict(float)
print(dic["a"])
print(dic.get("a"))
print(type(dic))
print(dic)

print("str=============")

dic = defaultdict(str)
print(dic["a"])
print(dic.get("a"))
print(type(dic))
print(dic)

print("str=============")

dic = defaultdict(int)
dic["a"] += 100
print(dic.get("a"))
print(type(dic))
print(dic)

print("=============")


def init_dic1(word):
    counter = {}
    for i in word:
        if i not in counter:
            counter[i] = 0
    return counter


def init_dic2(word):
    counter = {}
    for i in word:
        counter.setdefault(i, 0)
    return counter


def init_dic3(word):
    counter = defaultdict(lambda : 0)
    for i in word:
        counter[i] += 1
    return counter


def count_alpha1(lst):
    counter = defaultdict(list)
    for i in range(len(lst)):
         counter[len(lst[i])].append(lst[i])
    print(counter)


def count_alpha2(words):
    counter = defaultdict(set)
    for i in words:
        length = len(i)
        counter[length].add(i)
    print(counter)


if __name__ == "__main__":
    #dic_result = init_dic1("abcdedfg")
    #dic_result = dict(init_dic2("abcdedfg"))
    #dic_result = init_dic3("abcdedfg")

    #print(dic_result)
    lst1 = ["Python", "Ruby", "Java", "JavaScript", "R", "F", "CSharp", "CPlus", "C", "TypeScript"]
    count_alpha1(lst1)

    set1 = {"Banana", "Apple", "Orange", "Peach", "Melon", "Watermelon", "Pineapple", "Kiwi"}
    count_alpha2(set1)

    lst2 = [("Red", 1), ("Blue", 2), ("Yellow", 3), ("Brown", 4), ("Green", 5)]
    dic = defaultdict(list)

    for k, v in lst2:
        dic[k].append(v)

    for key, value in dic.items():
        print("{}, {}".format(key, value))
print("=============")


