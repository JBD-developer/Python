###############################
# TITLE : data structure
# CREATE DATE : 2022-02-04
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# stack Last In First Out
# POP PUSH

stack_data = []
# stack push
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)

# stack pop
print(stack_data.pop(-1))
print(stack_data.pop(0))
print(stack_data)

# word = input("Enter the message")
# stack_word = list(word)
# reverse_word = []
# for _ in range(len(stack_word)):
#     reverse_word.append(stack_word.pop())
# print(reverse_word)


def stack_push(data, n):
    data.append(n)


def stack_pop(data):
    if len(data) > 0:
        return data.pop()
    else:
        print("Error")
        return


def stack_push_data(stack):
    for i in range(1, 5):
        stack_push(stack, i)
        print("Stack state", stack)


def stack_pop_data(stack):
    for i in range(1, 5):
        stack_pop(stack)
        print("Stack state", stack)


if __name__ == "__main__":
    stack = []
    stack_push_data(stack)
    stack_pop_data(stack)
