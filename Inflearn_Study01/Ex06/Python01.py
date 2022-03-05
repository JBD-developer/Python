###############################
# TITLE : File Exception
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

"""
    open mode
    r  - read
    w  - write
    a  - append
    r+ - read & write
"""
# read
"""
Read 
file = open("E:\\workSpace_Etc\\TextFile\\yesterday.txt", "r")
file = open("E:\\workSpace_Etc\\TextFile\\yesterday.txt", "r", encoding="UTF-8")
line = file.readline().rstrip()
while line != "":
    print(line)
    line = readfile.readline().rstrip()
readfile.close()
"""

# write
"""
file = open("E:\\workSpace_Etc\\TextFile\\input.txt", "w")
file.write("Life is too short you need python")
file.close
"""

# append
"""
file = open("E:\\workSpace_Etc\\TextFile\\input.txt", "a")
file.write("Hello world\n")
print("Language", file=file)
file.close
"""

# close file
"""
# close 
file = open("E:\\workSpace_Etc\\TextFile\\input.txt", "a")
file.write("Hello world\n")
print("Language", file=file)
file.close
"""

"""
# try ~ finally
try:
    file = open("E:\\workSpace_Etc\\TextFile\\input.txt", "a")
    file.write("Hello world\n")
    print("Language", file=file)
finally:
    print("file close")
    file.close
"""

"""
# with 
with open("E:\\workSpace_Etc\\TextFile\\input.txt", "a") as file:
    file.write("Hello world\n")
    print("Language", file=file)
"""

sales_num = []
total_num = 0
with open("Ex06_File/test01.txt", "r") as file:

    line = file.readline().rstrip()

    while line != "":
        print(line)
        sales_num.append(int(line))
        line = file.readline().rstrip()

    print(sales_num)

    for i in sales_num:
        print(i)

    print(sum(sales_num) / len(sales_num))
    outfile = open("E:\\workSpace_Etc\\TextFile\\result.txt", "w")
    outfile.write("Total sales point : %d" %sum(sales_num) + "\n")
    outfile.write("average point : %f" % (sum(sales_num)/len(sales_num)))
    outfile.close()
