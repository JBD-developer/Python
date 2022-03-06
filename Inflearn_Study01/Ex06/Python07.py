###############################
# TITLE : File CWD(Current Working Directory)
# CREATE DATE : 2022-03-06
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

import csv

# cvs
"""
with open("Ex06_File\\test05.csv", "r", encoding="UTF-8") as weather:
    data = csv.reader(weather)
    header = next(data)
    temperature = 1000
    year = ""
    for row in data:
        if temperature > float(row[3]):
            temperature = float(row[3])
            year = row[0]
        print(row)

    print(year, temperature)
"""

# CWD

import os
dir = os.getcwd()
print(dir)
for filename in os.listdir():
    print(filename)

for filename in os.listdir():
    if os.path.isfile(filename):
        print("File", filename)

for filename in os.listdir():
    if os.path.isfile(filename):
        if filename.endswith(".py"):
            print(filename)

# image copy
# rb
# wb
infile = open("Ex06_File\\icon1.png", "rb")
outfile = open("Ex06_File\\icon1_copy.png", "wb")

while True:
    copy_buffer = infile.read(1024)
    print(copy_buffer)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
