###############################
# TITLE : string
# CREATE DATE : 2022-02-09
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# string

# slicing

word = "Life is too short, You need Python"
word1 = word[0:100]
print(word1)
print("================")
print("apple" < "banana")
# ord : character -> ascii
print(ord("a"))
print(ord("b"))

# chr : ascii -> character
print(chr(97))
print(chr(99))

# string method
# split()
message = "Life is too short, You need Python"
list_message = message.split()
print(list_message)

print("================")

message = "Life,is,too,short,You,need,Python"
list_message = message.split(",")
print(list_message)

print("================")

import regex
# regex
message = "Life/is|too/short|You%need%Python"
# list_message = message.split("/,|")
list_message = regex.split("[/,|%]", message)
print(list_message)

print("================")

#string check
# isalpha()
string = "abcde1"
print(string.isalpha())

# isdigit/isdecimal
string = "12345"
print(string.isdigit())
print(string.isdecimal())

# isalnum
string = "12334abcde"
print(string.isalpha())
print(string.isdigit())
print(string.isalnum())

# isspace
string = "     "
print(string.isspace())
print("================")

# endswith / startswith

# string = input("Enter the python source")
#
# if string.endswith(",py"):
#     print("This is a valid file name.")
# else :
#     print("This is a valid file name.")

filename = "2021-02-09.txt"
if filename.startswith("2022"):
    print("This is the 2022 file")
else:
    print("It\'s not a 2022 file.")

# upper / lower / capitalize / title
string = "test"

print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())

print("================")

# string format
string = "{}b{}"
print(string.format("a", "c"))

print("================")

# join()
list_string = ["a", "b", "1", "2"]
print("!".join(list_string))

# partition()
string = "python@python.co.kr"
tuple_string = string.partition(("@"))
print(type(tuple_string))

# count
string = "aaaabbbbcccc"
print(string.count("a"))
print(string.count("b"))
print(string.count("c"))

print("================")

# find / index

string = "apple"
print(string.find("z"))
print(string.index("a"))

print("================")

# lstrip() / strip() / rstrip()

string =  "     aaaa     bbbb  cccccc      "
print(string.lstrip())
print(string.rstrip())
print(string.strip())