# -*- coding: utf-8 -*-
#ifelse

n1=129
n2=123

if(n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")
    

std=int(input("enter your standard"))

if(std==1):
    print("You are in B.Tech 1st year")
elif (std==2):
    print("You are in B.Tech 2nd year")
elif (std==3):
    print("You are in B.Tech 3rd year")
else:
    print("You are in other standards")


#while and for
    
start=1
end=10

while(start<end):
    print(start)
    start+=1
    
for i in range(10):
    print(i)
    
for i in range(10,20):
    print(i)
    
for i in range(10,30,2):
    print(i)
    
for i in range(20,10,-1):
    print(i)