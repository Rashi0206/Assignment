# -*- coding: utf-8 -*-
name=input("Enter your name:")
print(type(name))
print("Your name is",name)

age=int(input("Enter your age:"))
print(type(age))
print("Your age is",age)

amount=float(input("Enter amount:"))
print(type(amount))
print("You have to pay",amount)

#operators
# + , _ , * , / , % , = , += ,*= ,//

n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
sum=n1+n2
print("sum of 2 numbers",n1,n2,"is",sum)

print(10/3)
print(10//3)

sum=0
sum=sum+10
sum+=10
print(sum)

#relational
# < , > , <= , >= ,!=

n1=123
n2=129
print(n1>n2)
print(n1!=n2)

# == , ===

n3=123
print(n1==n3)

#logical operators
# and , or , not

print(n1>n2 and n1>n3)

