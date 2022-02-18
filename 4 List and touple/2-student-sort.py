#write a program to accept marks of 6 students and display them in a sorted manner 

s1 = int(input('enter mark 1 : '))
s2 = int(input('enter mark 2 : '))
s3 = int(input('enter mark 3 : '))
s4 = int(input('enter mark 4 : '))
s5 = int(input('enter mark 5 : '))
s6 =int(input('enter mark 6 : '))

mylist = [s1, s2, s3, s4, s5, s6]
mylist.sort()
print('the sorted list are' , mylist)