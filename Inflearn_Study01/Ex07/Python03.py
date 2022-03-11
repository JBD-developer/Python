###############################
# TITLE : lambda
# CREATE DATE : 2022-03-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

f = lambda x, y, z: (x + y) * z

print(type(f))
print(f(10, 20, 30))

list_a = [1, 2, 3, 4, 5]
f2 = lambda x: x * 2
result_list = list(map(f2, list_a))
print(result_list)

result_list2 = list(map(lambda x : x * 2, list_a))
print(result_list2)

result_list2 = list(filter(lambda x : x % 2 != 0 , [i for i in range(1, 30)]))
print(result_list2)

data = [(3, 200), (3, 100), (1, 300), (2, 100), (2, 200)]
print(data)
sort_data = list(sorted(data, key=lambda data:data[0]))
print(sort_data)

# reduce
import functools

result = functools.reduce(lambda x, y : x + y, [1, 2, 3, 4])
print(result)
print("="*30)

orders = [[1, "Jacket", 5, 120000],
         [2, "Shirt", 6, 24000],
         [3, "Pants", 3, 50000],
         [4, "Coat", 6, 300000]
          ]

for items in orders:
    for values in items:
        print(values)
    print()

result = list(map(lambda x : (x[0],x[2] * x[3]), orders))
print(result)
print("="*30)

score_list = [("국어", 89), ("수학", 99), ("과학", 82), ("영어", 100)]
result_list = sorted(score_list, key=lambda x: x[1])
print(result_list)

filter_list = list(filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(filter_list)

result_list = list(map(lambda x : x ** 3, [i for i in range (1, 11)]))
print(result_list)

