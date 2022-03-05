###############################
# TITLE : File Exception
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# write()
# writelines()
# writeline()

with open("Ex06_File\\test03.txt", "w") as file :
    # for i in range(1, 10):
    #     file.write(str(i))
    #     file.write("\n")

    file.writelines(["1", "2", "3", "4", "5", "6"])
    file.writelines("\n")

    file.writelines("\n".join(["1", "2", "3", "4", "5", "6"]))
    file.writelines("\n")

with open("Ex06_File\\test02.txt", "r") as file:
    print(file.tell())
    print(file.read())
    print(file.tell())
    print("===="*30)
    print(file.seek(5))
    print(file.tell())
    print(file.read(10))