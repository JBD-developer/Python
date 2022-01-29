###############################
# TITLE : list comprehensions
# CREATE DATE : 2022-01-29
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
from math import *
list01 = [ x ** 2 for x in range(10)]
print("list01 :", list01)

list02 = []
for i in range (0 , 10):
    list02.append(i ** 2)
print("list02 :", list02)

list03 = [ "list"+ str(i) for i in range(1, 100)]
print(list03)

list04 = [x *3 for x in range (1, 10)]
print(list04)

list05 = [ x for x in range(10) if x % 2 == 0 and x != 0]
print(list05)

list06 = ["Java", "C#" , "CPlusPlus", "C", "JavaScript", "Python", "Riby", "R", "HTML"]
words = [word[0] for word in list06]
print(words)

message = "If the implementation is easy to explain, it may be a good idea".split(" ")

list_message = [len(word) for word in message]
print(list_message)

language = ["Java", "C#" , "CPlusPlus", "C", "JavaScript", "Python", "Riby", "R", "HTML"]
version = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

language_version = [(x, y) for x in language for y in version]
print(language_version)

squares = []

for x in range(1, 11):
    squares.append(pow(x, 2))

print(squares)

li_squares = [ round(pow(x,2)) for x in range(1, 11)]
print(li_squares)

odd_list = [x for x in range (1, 20) if x % 2 == 1]
print(odd_list)

even_list = [x for x in range (1, 20) if x % 2 ==0 ]
print(even_list)

gugu_list = [(x * y ) for x in range (2, 10)
                      for y in range (1, 10) ]
print(gugu_list)

list_test1 = ["Red", "Yellow", "Blue", "Pink", "Black", "Brown"]

list_first = [word[0] for word in list_test1]
print(list_test1)
print(list_first)
list_last = [word[-1] for word in list_test1]
print(list_last)
list_length = [len(word) for word in list_test1]
print(list_length)

list_catasian = [ x+"-"+str(y) for x in list_test1
                       for y in list_length]
print(list_catasian)

# -------
# print Friends list
# Add Friend
# Delete Friend
# Update Friend
# Exit
#----------

list_friends = []
input_num = ""
while True :
    print("1 - Friends list\n" 
          "2 - Add Friend\n"
          "3 - Delete Friend\n"
          "4 - Update Friend\n"
          "5 - Exit\n" )

    input_num = int(input("Enter the number"))

    if input_num == 5:
        print("Exit")
        break;

    elif input_num == 1:
        if len(list_friends) == 0 :
            print("you don't have any friends on my friend list")
        else:
            for i in range(len(list_friends)):
                print(list_friends[i])

    elif input_num == 2:
        friend_name = input("Enter the friend name")
        list_friends.append((friend_name))

    elif input_num == 3:
        friend_name = input("Enter the friend name")
        if friend_name in list_friends:
            list_friends.remove(friend_name)
        else :
            print("The name is not correct")
    elif input_num == 4:
        friend_name = input("Enter the friend name")

        if friend_name in list_friends:
            index = list_friends.index(friend_name)
            friend_name = input("Enter the friend new name")
            print(friend_name)
            list_friends[index] = friend_name
            print(index)
            print(list_friends[index])
        else :
            print("The name is not correct")
    else :
        print("Error")


