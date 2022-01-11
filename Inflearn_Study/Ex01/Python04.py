###############################
# TITLE : Data type
# CREATE DATE : 2022-01-10
# CREATOR : J
# MODIIFIER :
# MODIFY DATE
# VERSIOM : 1.0.0
###############################

#double quotation
welcome1 = "Happy new year 2022"
print(welcome1)

#Single quotation
welcome1 = 'Happy new year 2022'
print(welcome1)

welcome2 = "'Happy new year 2022'"
print(welcome1)
print(welcome2)

message = "doesn\'t"
print(message)
message = "\"Yes, I Can do it\""
print(message)

#escape

#n
message = 'First\nSecond\nThird'
print(message)

#t
path = "c:\temp\name"
print(path)
path2 = r"c:\temp\name\file.txt:"
print(path2)

message = "world"
print("world Length : ", len(message))
print(0, message[0])
print(1, message[1])
print(2, message[2])
print(3, message[3])
print(4, message[4])

firstName = "PARK"
lastName = " JISUNG"
fullName = firstName + lastName
print(fullName)

tempStr = "Person" + str(100)
print(tempStr)

print(("-" * 10), ">")

price = 20000
print("Price : %s" % price)
nowTime = "%s Hour : %s Minute : %s Second"
print(nowTime % (8, 6, 15))

#Indexing
fullName = 'Liverpool'
print(fullName, 0, fullName[0])
print(fullName, 1, fullName[1])
print(fullName, 2, fullName[2])
print(fullName, 3, fullName[3])
print(fullName, 4, fullName[4])
print(fullName, 5, fullName[5])
print(fullName, 6, fullName[6])
print(fullName, 7, fullName[7])
print(fullName, 8, fullName[8])
print()

print(fullName, -1, fullName[-1])
print(fullName, -2, fullName[-2])
print(fullName, -3, fullName[-3])
print(fullName, -4, fullName[-4])
print(fullName, -5, fullName[-5])
print(fullName, -6, fullName[-6])
print(fullName, -7, fullName[-7])
print(fullName, -7, fullName[-8])
print(fullName, -9, fullName[-9])

lastStr = (fullName[len(fullName)-1])
print("Last Index string : ", lastStr)
#string index out of range

strO = input()
strS = input()
strT = input()

fullWord = strO[0] + strS[0] + strT[0]
print (fullWord)




