###############################
# TITLE : Iterator Generator
# CREATE DATE : 2022-03-12
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

list1 = [10, 20, 30]

list1_iter = iter(list1)

print(list1_iter.__next__())
print(list1_iter.__next__())
print(list1_iter.__next__())
print(list1_iter.__next__())