###############################
# TITLE : File counting
# CREATE DATE : 2022-03-05
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

counter = [0] * 26
print(type(counter))

"""
with open("Ex06_File\\test07.txt", "r") as mobydick :
    ch = mobydick.read(1)
    while ch != "":
        ch = ch.upper()
        if ch >= "A" and ch <= "Z":
            print(ch)
            # ord() is alphabet return 
            i = ord(ch) - ord("A")
            counter[i] += 1
        ch = mobydick.read(1)
    print(counter)
"""
dic = {}
with open("Ex06_File\\test07.txt", "r") as loadfile :
    for word in loadfile:
        print("word : ", word)
        for char in word.strip():
            print("char : ", char)
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
    print(dic.items())