###############################
# TITLE : File Exception
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

with open("Ex06_File\\test02.txt", "r", encoding="UTF-8") as file:
    # 1 read()
    # file = file.read()
    # print(file)

    # 2 readline()
    # line = file.readline()
    #
    # while line != "":
    #     line = file.readline()
    #     print(line, end=' ')

    # 3 readlines()
    line = file.readlines()
    print(type(line))
    result = ''.join(line)
    print(result)