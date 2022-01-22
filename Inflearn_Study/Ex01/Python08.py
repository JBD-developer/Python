###############################
# TITLE : string
# CREATE DATE : 2022-01-22
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# string
fruit = "apple"

for letter in fruit:
    print(letter, " ")

# message = input("Enter the message \n :")
# vowels = "aeiouAEIOU"
# consonant = ""
# for letter in message :
#     if letter not in vowels :
#         consonant += letter
#         print(letter)
# print(consonant)
#
# message = input("Enter the message \n :")
# word = message.lower()
# vowels = "aeiou"
# consonant = ""
# iCountCon = 0
# iCountVow = 0
#
# if len(message) > 0 and message.isalpha():
#     for letter in message:
#         if letter not in vowels:
#             consonant += letter
#             iCountCon += 1
#         else:
#             iCountVow += 1
#
# print("consonant\'s count : %d \n vowels\'count : %d" % (iCountCon, iCountVow))

# numAlpha = 0
# numNumber = 0
# numSpace = 0
#
# message2 = input("Enter the message \n :")
#
# for letter in message2:
#     if letter.isalpha():
#         numAlpha += 1
#     elif letter.isdigit():
#         numNumber += 1
#     elif letter.isspace():
#         numSpace += 1
#
# print("Number count : %d \n Alpha count : %d \n space count : %d " %(numNumber, numAlpha, numSpace))

# tel = input("Enter the phone number Ex) 000-0000-0000")
# removeTel = ""
# if  len(tel) == 12 or len(tel) == 11:
#     for letter in tel:
#         if letter != "-":
#             print(letter)
#             removeTel += letter
#
#     print(removeTel)
# else :
#     print("Error")

# message = input("Enter the message\n")
result = ""
#
# for letter in message:
#     if letter != " ":
#         result += letter
# print(result)
#
# for letter in message :
#     result = letter + result
# print(result)

# s_list = list(message)
#
# print(type(s_list))
# print(s_list)
# s_list.reverse()
# print("".join(s_list))
#
# s1 = message
# print("".join(reversed(s1)))
# print(message[::-1])
# print(message[3::-1])

statement = "*********Hello"
print(statement)
print(statement.lstrip("*"))

statement = "Hello*********"
print(statement)
print(statement.rstrip("*"))

statement = "********Hello**********"
print(statement)
print(statement.strip("*"))

statement = "Hello world Python Study"
print(statement.split())
