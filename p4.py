# -*- coding: utf-8 -*-
#Reverse order of 12 table

n1=12
for i in range(10,0,-1):
    result=n1*i
    print(n1,"*",i,"=",result)


#Simple Interest
    
p=float(input("Enter principal amount"))
r=float(input("Enter rate"))
t=int(input("Enter time in years"))
SI=(p*t*r)/100
print("Simple Interest=",SI)

#Prime Number

n1=int(input("Enter starting number"))
n2=int(input("Enter ending number"))
for i in range(n1,n2):
    n1%i
    if(n1%i==0):
        print(n1)