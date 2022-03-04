###############################
# TITLE : collections module
# CREATE DATE : 2022-02-13
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

from collections import defaultdict
from collections import OrderedDict


def file_Read(text):
    f_name = open("E:\\workSpace_Etc\\dummy.txt", mode="r", encoding="UTF-8")

    for line in f_name:
        words = line.strip().split()
        for word in words:
            if len(word) >= 2 :
                text.append(word)
    print(text)

if __name__ == "__main__":
    text = []
    file_Read(text)
    word_count = defaultdict(lambda : 0)

    for word in text:
        word_count[word] += 1

    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t :t[1], reverse=True)).items():
        print(i, v)
