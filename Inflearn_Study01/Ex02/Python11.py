###############################
# TITLE : double list
# CREATE DATE : 2022-02-03
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

double_list = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]
               ]

total = 0

for i in range(len(double_list[0])):
    total += double_list[0][i]
print("Rows sum : ",total)

total = 0
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        total += double_list[i][j]
print("All rows sum : ", total)


def print_init(li):
    for row in range(len((li))):
        for col in range(len(li[row])):
            if(row+col)%2 ==0:
                li[row][col] = 1

def print_list(li):
    for row in range(len((li))):
        for col in range(len(li[row])):
            print(li[row][col], end=" ")
        print()


if __name__ == "__main__":
    # table = []
    # for row in(range(10)):
    #     table +=[[0]* 10]
    # print_init(table)
    # print_list(table)
    kor_total = 0
    eng_total = 0
    math_total = 0

    total_sum = 0
    avg = 0.0

    score_list = [
                    [100, 100, 100],
                    [20, 20, 20],
                    [30, 30, 30],
                    [40, 40, 40],
                    [50, 50, 50]
                ]



for i in range(len(score_list)):
    sum = 0
    average = 0.0
    kor_total += score_list[i][0]
    eng_total += score_list[i][1]
    math_total += score_list[i][2]


    print("%3d" % (i+1), end="\t")
    for j in range(len(score_list[i])):
        sum += score_list[i][j]
        print("\t%d" %score_list[i][j], end="\t")

    total_sum += sum
    average = sum/ len(score_list[i])

    avg += average
    print("\t%d\t\t%.2f" %(sum, average))

avg / len(score_list)

print("Total\t%d\t%d\t%d\t%d\t%.2f" % (kor_total, eng_total, math_total, total_sum, avg))

