###############################
# TITLE : list
# CREATE DATE : 2022-01-28
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

#list

score_list = []

score_list.append(30)
print("append scorelist value integer :", score_list)
score_list.append("Python")
print("append scorelist  value string :", score_list)
score_list.append(3.141592)
print("append scorelist  value float :", score_list)

print("scorelist length :", len(score_list))

score_list[0] = 35
print("scorelist index 1 update", score_list)

index = 0
for i in range(len(score_list)) :
        print(index + 1, score_list[i])
        index += 1

for i in score_list:
    print(i)


num_list = []
# for i in range(5):
#     num_list.append(int(input("Enter the integer\n:")))
#
# print(num_list)

li1 = list()
print("li1", li1)
li2 = list("Hi")
print("li2", li2)
li3 = list(range(0, 5, 2))
print("li3", li3)
li4 = [["Seoul", 10], ["Tokyo", 40], ["Newyork", 50]]
print("li4", li4)
print("li4[0][0]", li4[0][0])
print("li4[0][1]", li4[0][1])
print("li4[1][0]", li4[1][0])
print("li4[1][1]", li4[1][1])
print("li4[2][0]", li4[2][0])
print("li4[2][1]", li4[2][1])

for i in range(len(li4)):
    for j in range(len(li4[i])):
        print(li4[i][j])

score_80_count = 0
score_avg = 0.0
score_list = []
score_total = 0

for i in range(4):
    score = int(input("Enter the score\n"))
    score_total += score
    score_list.append(score)
    if score_list[i] >= 80:
        score_80_count += 1

score_avg = score_total // len(score_list)
print("Top ", score_80_count)
print("Avg ", score_avg)
print(score_list)

dog_list = []
while True:
    dog_name = input("Enter the dog name : \n")
    if dog_name == "":
        break
    print(dog_name)
    dog_list.append(dog_name)
print(dog_list)