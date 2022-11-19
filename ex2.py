# Exercise 2 - Faulty Calculator

'''45+3=555, 56+9=77,56/6=4
Design a calculator which will correctly solve all the problems except
the following ones:
45+3=555,56+9=77,56/6=4
your program should take operator and the two numbers as input from the user
and then return the result'''

'''x=int(input(""))
y=int(input(""))
z=int(input(""))
for x==48:
    print(555)
for (y==65):
    print(77)
for (z==9.33):
    print(4)'''

print("Enter 1st Number")
num1 = int(input())
print("Enter 2nd Number")
num2=int(input())
print("so what you want?","+,-,/,*,%")
num3 = input()

if num1==45 and num2==3 and num3=="+":
    print(555)
elif num1==56 and num2==9 and num3=="+":
    print(77)
elif num1==56 and num2==6 and num3=="/":
    print(4)

