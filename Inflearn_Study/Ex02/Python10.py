###############################
# TITLE : double list
# CREATE DATE : 2022-01-31
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# rows = 3
# cols = 5
#
# list = []
#
# for row in range(rows):
#     list += [[0] * cols]
# print(list)
#
# list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
#
# for i in range (len(list)):
#     for j in range (len(list[i])):
#         print(list[i][j])

double_list = [
                [1, 2, 3, 4, 5, 6 ],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18]
              ]
print(double_list)
print(double_list[0])
print(double_list[1])
print(double_list[2])

print(id(double_list))
print(id(double_list[0]))
print(id(double_list[1]))
print(id(double_list[2]))

print(len(double_list))
print(len(double_list[0]))
print(len(double_list[1]))
print(len(double_list[2]))


for i in range (len(double_list)):
    for j in range (len(double_list[i])):
        print(double_list[i][j], end="\t")
    print()


rows = int(input("Enter the rows"))
cols = int(input("Enter the cols"))

list = []

for row in range(rows):
    list += [[0] * cols]
print(list)

list2  = [([0] *cols) for row in range(rows)]
print(list2)

list3 =[1, 2, 3]
list3[0] = 10

print(list3)

list4 = [[1, 2], [3,4]]
list4[0][1] = -7
print(list4)