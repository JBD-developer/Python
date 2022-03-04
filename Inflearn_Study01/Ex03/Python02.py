###############################
# TITLE : data structure
# CREATE DATE : 2022-02-04
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# queue First In First Out
# OFFER POLL

queue_data = []
queue_data.append(10)
queue_data.append(20)
queue_data.append(30)
queue_data.append(40)
queue_data.append(50)
print(queue_data)

queue_data.pop(0)
print(queue_data)


def queue_offer(data, n):
    data.append(n)


def queue_poll(data):
    if len(data) > 0:
        return data.pop(0)
    else:
        print("Error")
        return


def queue_offer_data(data):
    for i in range(1, 5):
        queue_offer(data, i)
        print("Queue state:", data)


def queue_poll_data(data):
    for i in range(1, 5):
        queue_poll(data)
        print("Queue state:", data)


if __name__ == "__main__":
    queue = []
    queue_offer_data(queue)
    queue_poll_data(queue)