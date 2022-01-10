###############################
# TITLE : Data type
# CREATE DATE : 2022-01-10
# CREATOR : J
# MODIIFIER :
# MODIFY DATE
# VERSIOM : 1.0.0
###############################

from math import *

strName = 'Hello World'
print(type(strName))
numX = 17
print(type(numX))
numY = 3.1452
print(type(numY))

#4.0 / 3.0 * pi * r ** 3
radius = 5.0
volume = 4.0 / 3.0 * pi * (pow(radius, 3))
print(volume)
print(pi)

#4 * pi * r ** 2
outer_area = 4 * pi * pow(radius, 2)
print('The outer width of a sphere : ', outer_area)
print('The outer width of a sphere : ' + str(outer_area))
#End of File : EOF

# Speed of light 300000
distance = 40 * pow(10, 12)
print(distance)

seconds = (distance/300000)
print('Second', seconds)
lightYear = seconds/(60 * 60 * 24 * 365)
print('Year', lightYear)

print(10 == 10.0)
print(10 == '10')

itemPrice = int(input('Price : '))

bill_1000 = int(input('1000 : '))
coin_500 = int(input('500 : '))
coin_100 = int(input('100 : '))

nod_money = ((bill_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - itemPrice
print(nod_money)
nCoin500 = nod_money // 500
nod_money = nod_money % 500

nCoin100 = nod_money // 100
nod_money = nod_money % 100

nCoin50 = nod_money // 50
nod_money = nod_money % 50

nCoin10 = nod_money // 10
nod_money = nod_money % 10


nCoin1 = nod_money
print("500", nCoin500, "100", nCoin100, "50", nCoin50, "10", nCoin10, "1", nCoin1)

