# -*- coding: utf-8 -*-

#Sum of elements in the list

s=0
data=[2,4,1,47,38]
for i in range(0,5):
    s+=data[i]
print("Sum of elements in list:",s)


# Maximum element in list

data=[2,4,1,47,38]
max=data[0]
for n in data:
    if(n>max):
        max=n
print(max)


# Minimum element in list

data=[2,4,1,47,38]
min=data[0]
for n in data:
    if(n<min):
        min=n
print(min)


# Average of elements in the list

data=[2,4,1,47,38]
sum=0
for i in range(0,5):
    sum+=data[i]
    avg=sum/5
print(avg)


#Search an element in list

data=[2,4,1,47,38]
flag=0
sele=int(input("Enter the element to be searched:"))
for i in data:
    if(sele==i):
        flag=1
        print(sele,"is present")
    else:
        continue
if(flag==0):
    print(sele,"not found")
        