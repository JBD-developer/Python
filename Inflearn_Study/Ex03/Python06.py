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

# palindrome
# string = input("Enter the string")
#
# result = ""
# for i in range(len(string)):
#     result = string[i] + result
#     print(result)
#
# if result == string:
#     print("palindrome")
# else:
#     print("Not palindrome")
#

def check(s):
    low = 0
    high = len(s)-1

    while True:

        if low > high:
            return True

        s1 = s[low]
        s2 = s[high]
        print(s1, s2)
        if s1 != s2 :
            return False

        low += 1
        high -= 1


def check_count(s):

    dic_count = {"digits": 0, "spaces": 0, "alpha": 0}

    for i in range(len(s)):
        word = s[i]
        print(word)

        if word.isalpha():
            dic_count["alpha"] += 1
        elif word.isdigit():
            dic_count["digits"] += 1
        elif word.isspace():
            dic_count["spaces"] +=1

    print(dic_count)


def check_acronym():
    string  = input("Enter the word")
    acronym = ""
    for word in string.upper().split():
        acronym += word[0]

    print("acronym : ", acronym)

def check_csv():

    fp = open("E:\\workSpace_Etc\\Test1.csv", mode="r", encoding="UTF-8")

    for line in fp.readlines():
        line = line.strip()
        print(type(line))


        words = line.split(",")
        for word in words :
            print(word, " ")
    fp.close()


if __name__ == "__main__":
    # st = input("Enter the string")
    # st = st.replace(" ", "")
    #
    # if check(st) == True:
    #     print("palindrome")
    # else:
    #     print("Not palindrome")
    #st = input("Enter the string")
    #check_count(st)
    check_acronym()
    check_csv()