
"""
ch=4

1. Write a program to store seven fruits in a list entered by the user. 
2. Write a program to accept marks of 6 students and display them in a sorted 
manner. 
3. Check that a tuple type cannot be changed in python. 
4. Write a program to sum a list with 4 numbers. 
5. Write a program to count the number of zeros in the following tuple:
         a = (7, 0, 8, 0, 0, 9) 
"""

fruitNAME=["apple","guava","watermelon","mango","Lichi"]
print(fruitNAME)

lis=[]
print(lis)
marks1=int(input("enter marks1:"))
lis.append(marks1)
marks2=int(input("enter marks2:"))
lis.append(marks2)
marks3=int(input("enter marks3:"))
lis.append(marks3)
marks4=int(input("enter marks4:"))
lis.append(marks4)
marks5=int(input("enter marks5:"))
lis.append(marks5)
marks6=int(input("enter marks6:"))
lis.append(marks6)
print(lis)
lis.sort()
print(lis)
print(type(lis))

#3
fruits=("apple","guava","watermelon","mango","Lichi")
print(fruits)
print(type(fruits))
fruitsinLIST=list(fruits)
print(type(fruitsinLIST))

lis=[1,2,3,4]
print(lis)
print(lis[0])
print(lis[1])
print(lis[2])
print(lis[3])
print("sum=",lis[0]+lis[1]+lis[2]+lis[3])

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
print(a.count(1))
print(a.count(9))
