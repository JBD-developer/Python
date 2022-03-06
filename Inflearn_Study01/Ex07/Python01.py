###############################
# TITLE : Built in function
# CREATE DATE : 2022-03-06
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# abs()
num = -20
print(abs(num))

# all() / any()
dic = {"A":1, "B":2, "C":0}
lst = [1, 0, 2, 3, 5]
print(all(dic))
print(any(dic))
print(all(lst))
print(any(lst))

# bin()
print(bin(abs(num)))

#eval()
# exp = eval(input("Enter the formula"))
# print(exp)

#sum() len()
lst = [1, 2, 3, 4, 5]
print(sum(lst))
print(len(lst))

# list()
msg = "Hello Python"
lst = msg.split()
print(lst)

#map()
def square(n):
    return n * n
lst = [1, 2, 3, 4, 5]
tup = (1, 3, 4, 5)

result1 = list(map(square, lst))
result2 = list(map(square, tup))
print(result1)
print(result2)
print("="*30)


# dir()
print(dir([1, 2, 3]))

# max() min()
print(max(lst))
print(min(lst))

# enumerate()
season = ["Spring", "Summer", "Fall", "Winter"]
print(list(enumerate(season)))
print(list(enumerate(season, start=1)))



# filter()
def myfilter(x):
    return x > 3

result = filter(myfilter, [1, 2, 3, 4, 5, 6])
print(list(result))

#zip()
num_key = [1, 2, 3, 4]
num_value = ["one", "two", "three", "four"]

print(list(zip(num_key, num_value)))

dic = {}

for n, s in zip(num_key, num_value):
    dic[n] = s

print(dic)

lst_name = ["Mike", "Kane", "JEONG", "KIM"]
lst_num = [1, 3, 0, 6]
total_num = sum(lst_num) + len(lst_name)
print("Total people :", total_num)

dic_info = {}
for name, num in zip(lst_name, lst_num):
    dic_info[name] = num

for key, value in dic_info.items():
    print(key, value)

def myfilter2(x):
    return x % 3 == 0

result = filter(myfilter2 , [i for i in range(1, 100)])
sum = sum([1 for i in range(1, 100) if i % 3 == 0 ])
print(list(result))
print(sum)

numX = eval(input("Enter the number"))
print(numX)