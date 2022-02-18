#write a program to find greatest fo four numbers entered by the user

num1 =int( input("Enter the number 1: "))
num2 =int( input("Enter the number 2: "))
num3 =int( input("Enter the number 3: "))
num4 =int( input("Enter the number 4: "))

if num1>=num4:
    f1 = num1
else: 
    f1 = num4

if(num2>=num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print('The greatest number is : '+ str(f1))
else:
    print('The greatest number is : '+ str(f2))