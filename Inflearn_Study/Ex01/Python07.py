###############################
# TITLE : Iteration
# CREATE DATE : 2022-01-11
# CREATOR : J
# MODIFIER : J
# MODIFY DATE : 2022-01-21
# VERSION : 1.0.0
###############################
import turtle

for x in range(10):
    print("Hello Python")

for name in ["BUSAN", "SEOUL", "DAEJEOM", "ULSAN", "DAEGUE"]:
    print("City name :", name )

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(x, end=",\t")

sum = 0
for x in range(10):
    print(x)
    sum += x
print(sum)

for char in "abcdefghi":
    print(char, end=",")

for x in range(6):
    print("------------")
    print("Hello Python")

print(type(range(5)))
print(range(5))

# range function
for x in range(1, 11):
    print(x)

for x in range(1, 11, 3):
    print(x)

title= "Code name is javaKiller"

for char in title:
    print(char, end="\t")
print()
for char in title:
    print(char, end="")

numX = int(input("Enter the integer\n"))
total1 = 0
for x in range(1, numX + 1):
    total1 += x
print(total1)

total2 = 0
for x in range(101):

    if total2 >= 2000:
        print(x)
        break
    total2 += x


# Factorial
fact = 1.0
numY = int(input("Enter the integer\n"))
for i in range(1 ,numY+1):
    fact *= i
print (numY, "Factorial :", fact)

# Fibonacci
n1 = 1
n2 = 1
n3 = 1

fibonacci = int(input("Enmter the Fibonacci \n" ))
for i in range(1, fibonacci):
    if i < 3:
        n3 = 1
    else :
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    if n3 < fibonacci:
        print(n3, end=",")

# C = (F - 32) * 5 / 9

for t in range(0, 101, 10):
    c = (t - 32) * 5.0 / 9.0
    print(t, ":\t ", round(c, 2))


# multiplication table

for i in range(1, 10):
    print(2,  "*", i, "=",(2 * i))

for i in range (2, 10):
    for j in range (1, 10):
        print(i, "*",j, "=", (i*j))


numX = int(input("Enter the integer\n"))
numY = int(input("Enter the integer\n"))
count = 0 ;
for i in range(numX, numY+1):
    if (i % 3 == 0) and (i % 4 == 0):
        continue
    count += 1
    print(count, "count :" , i)


p = turtle.Pen()

for i in range(50):
    p.forward(50)
    p.right(144)

for i in range(10):
    p.left(20)

    p.forward(50)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.left(90)


turtle.exitonclick()