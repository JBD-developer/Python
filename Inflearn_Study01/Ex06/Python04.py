###############################
# TITLE : File csv
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from collections import defaultdict

"""
with open("Ex06_File\\test04.txt", "r") as file:
    dic = defaultdict(lambda : 0)
    for line in file:
        line = line.rstrip()
        word_list = line.split()
        for word in word_list:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
    
    print (dic.items())
"""

"""
line = "apple,grape,banana,pear"
word_list = line.split(",")
print(word_list)
"""


with open("Ex06_File\\test06.txt", "r") as file:
    char = file.read(1)
    print(char)
    while char != "":
        print(char, end="")
        char = file.read(1)