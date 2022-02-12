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
from collections import OrderedDict

# OrderDict

dic1 = {}

dic1['a'] = 100
dic1['b'] = 110
dic1['c'] = 120
dic1['d'] = 130

# keys()
for i in dic1.keys():
    print(i)

# values()
for i in dic1.values():
    print(i)

# items()
for k, y in dic1.items():
    print(k, y)

print("================")

dic_order = OrderedDict()
dic_order['w'] = 10
dic_order['x'] = 20
dic_order['y'] = 30
dic_order['z'] = 40

for key, value in dic_order.items():
    print("[%s : %d]" % (key, value))

print("================")

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"A": 1, "C": 3, "B": 2}
print(dic1 == dic2)

print("================")

order_dic1 = OrderedDict({"A": 1, "B": 2, "C": 3})
order_dic2 = OrderedDict({"A": 1, "C": 3, "B": 2})
print(order_dic1 == order_dic2)

print("================")

order_dict3 = OrderedDict()
order_dict3["a"] = 1
order_dict3["b"] = 2
order_dict3["c"] = 3
order_dict3["d"] = 4
order_dict3["e"] = 5
order_dict3["f"] = 6
order_dict3["g"] = 7
order_dict3["h"] = 8

print(type(order_dict3))

for k, y in order_dict3.items():
    print(k, y)


print("================")

# sorted

def sort_by_key(t):
    return t[0]

dict3 = dict()
dict3["g"] = 7
dict3["h"] = 8
dict3["b"] = 2
dict3["c"] = 3
dict3["a"] = 1
dict3["d"] = 4
dict3["e"] = 5
dict3["f"] = 6

for k, y in dict3.items():
    print(k,y)

print(sorted(dict3.keys()))
list_keys = list(sorted(dict3.keys()))
list_values = list(sorted(dict3.values()))
print(list_keys)
print(list_values)
print(dict3)
li = sorted(dict3.items(), key=sort_by_key)
print(li)

for k, y in OrderedDict(sorted(dict3.items(), key=sort_by_key)).items():
    print(k, y)

print("================")

ordered_dict3 = OrderedDict()
ordered_dict3["g"] = 7
ordered_dict3["h"] = 8
ordered_dict3["b"] = 2
ordered_dict3["c"] = 3
ordered_dict3["a"] = 1
ordered_dict3["a"] = 1
ordered_dict3["e"] = 5
ordered_dict3["f"] = 6

print(type(order_dict3))


print("================")


