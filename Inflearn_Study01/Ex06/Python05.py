###############################
# TITLE : File csv
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import csv

# with open("Ex06_File\\test05.csv", "r", e) as temperature:
#     data = csv.reader(temperature)
#     # remove header
#
#     header = next(data)
#
#     for row in data:
#         print(row)

f = open("Ex06_File\\test05.csv", "r", encoding="UTF-8")
data = csv.reader(f)
header = next(data)
print(header)
for row in data:
    print(row)

f.close()