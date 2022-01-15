###############################
# TITLE : Variable
# CREATE DATE : 2022-01-09
# CREATOR : J
# MODIFIER :
# MODIFY DATE :
# VERSION : 1.0.0
###############################

num1 = 200
num2 = 300

print(type(num1))
print(type(num2))
print('Before num1 : ',num1, 'num2 : ',num2)

numTemp = num1
num1 = num2
num2 = numTemp
print('After num1 : ',num1, 'num2 : ',num2)

peopleNum = input("사용자의 인원을 입력해주세요")
chickens = int(peopleNum)
beer = int(peopleNum) * 2
cake =  int(peopleNum) * 3

print("chickens Number : ",chickens)
print("Beers Number : ",beer)
print("Cakes Number : ", cake)

numX = int(input("First Integer "))
numY = int(input("Second Integer "))
sum = numX + numY
sub = numX - numY
mul = numX * numY
div = numX / numY
print(sum)
print(sub)
print(mul)
print(div)

numMoney = 5000
numCandyPrice = 120
maxCandy = numMoney // numCandyPrice
reminder = numMoney % numCandyPrice
print(maxCandy)
print(reminder)