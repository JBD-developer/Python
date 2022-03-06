###############################
# TITLE : File Dictionary
# CREATE DATE : 2022-03-06
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import pickle
# dic
# dic = {"sound":8, "videoQuality":"King", "Money":10000, "WeaponList":["gun", "missle", "knife"]}
#
# with open("Ex06_File\\test08.dat", "wb") as file :
#     pickle.dump(dic, file)

with open("Ex06_File\\test08.dat", "rb") as file:
    obj = pickle.load(file)

    print(obj)
    for key, value in obj.items():
        print(key, value)


# Regular expression
import re

# with open("Ex06_File\\test09.txt","r") as file:
#     for line in file:
#         line = line.rstrip()
#         if re.search('^[0-9]+',line):
#             print(line)

text ="""101 COM Pytnon Programming
102 MAT LinearAlgebra
103 ENG Computer"""

s = re.findall("\d+", text)
for word in s :
    print(s)