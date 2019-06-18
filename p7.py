# -*- coding: utf-8 -*-

class student():
    def register(self,regno,name,standard,section):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.section=section
        
    def information(self):
        print("Regno",self.regno,"Name",self.name,"Standard",self.standard,"Section",self.section)
        
Mahan=student()
Mahan.register(129,"Mahan","9","B")
Mahan.information()

Manas=student()
Manas.register(77,"Manas","9","B")
Manas.information()

Mounish=student()
Mounish.register(85,"Mounish","9","B")
Mounish.information()

Preethish=student()
Preethish.register(109,"Preethish","9","B")
Preethish.information()


#Calculator

class calc():
    def add(self,num1,num2):
        return(num1+num2)
    def sub(self,num1,num2):
        return(num1-num2)
    def mul(self,num1,num2):
        return(num1*num2)
    def div(self,num1,num2):
        return(num1/num2)

c=calc()
result=c.add(10,20)
print("Addition is:",result)
result=c.sub(20,10)
print("Subtraction is:",result)
result=c.mul(12,6)
print("Multiplication is:",result)
result=c.div(78,9)
print("Division is:",result)