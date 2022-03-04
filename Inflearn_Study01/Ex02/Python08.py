###############################
# TITLE : list operator
# CREATE DATE : 2022-01-31
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# min max
s = [-1, -10, 10, 4, 11, 12, -3]

max_value = s[0]
min_value = s[0]

for i in range (1, len(s)):
    if min_value > s[i]:
        min_value = s[i]
print(min_value)

for i in range (1, len(s)):
    if max_value < s[i]:
        max_value = s[i]
print(max_value)

animal = ["dog", "lion", "bird", "tiger", "mouse"]
short_value = animal[0]
for i in range(1, len(animal)):
    if len(animal[i]) < len(short_value):
        short_value = animal[i]
print(short_value)

price = [1000, 3000, 500, 10000, 20000, 700]
min_price = price[0]
max_price = price[0]

for i in range(1, len(price)):

    if min_price > price[i]:
        min_price = price[i]

    if max_price < price[i]:
        max_price = price[i]

print(min_price, max_price)

js_list = ["Node", "Next", "Vanilla", "Angular", "React", "Javascript", "Vue"]
print(min(js_list))
print(max(js_list))
shortest_value = js_list[0]
shortest_list = []
for i in range(1, len(js_list)):
    if len(js_list[i]) <= len(shortest_value):
        if len(js_list[i]) <= len(shortest_value):
            shortest_list.clear()
            shortest_list.append((js_list[i]))
print("Shortest value", shortest_value)

print(shortest_list)

#Search
js_list = ["Node", "Next", "Vanilla", "Angular", "React", "Javascript", "Vue", "React"]
#
# search_word = input("Enter the name \n")
#
# if search_word in js_list:
#     index = js_list.index(search_word)
#     print("Index : ", index, "Name :" , search_word )
# else :
#     print("Not")

num_list = [10, 20, 30 , 40 , 50, 40, 70, 80, 90, 100, 100, 100, 100 ]
def number_search(list, key):
    cnt = 0
    for i in range(len(list)):
        if key == list[i]:
            cnt += 1
    return cnt

result = number_search(num_list, 110)
if result == 0:
    print("Not")
else :
    print(result)

print(number_search(num_list, 40))

