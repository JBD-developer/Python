###############################
# TITLE : list Sort
# CREATE DATE : 2022-01-31
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# inplace sort
#
# data_list = []
# fp = open("E:\\workSpace_Etc\\data.txt", mode="r", encoding="UTF-8")
#
# print(fp)
# print(type(fp))
#
# for line in fp.readline():
#     data_list.append(line.strip())
#
# fp.close()
# print(data_list)
#
# fp = open("E:\\workSpace_Etc\\data.txt", mode="w", encoding="UTF-8")
# fp.write("Python study")
#
# fp.close()

list1 = [4, 8, 9, -1, 10]
print(list1)
list1.sort()
print(list1)

def selectionSort(li):
    cnt = 0
    for i in range(len(li) -1):
        min_idx = i
        for k in range(i+1, len(li)):

            if li[min_idx] > li[k]:
                min_idx = k

        if min_idx != i:
            li[i], li[min_idx] = li[min_idx], li[i]
            cnt += 1
    print("Change count ", cnt)
    return li


def bubbleSort(li):
    list_length = len(li)
    for i in range(list_length - 1):
        for k in range(list_length - i - 1):
            if li[k] > li[k + 1]:
                li[k], li[k + 1] = li[k + 1], li[k]
    return li

if __name__ == "__main__":
    li = [4, 6, 1, 10, 7, -7, -100, 15, 30 , 15]
    selectionSort(li)
    print(li)

    bubbleSort(li)
    print(li)

