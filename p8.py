# -*- coding: utf-8 -*-

class Car():
    def __init__
    (self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.speed=0
        
    def start(self):
        self.speed=0
        return self.speed
        
    def move(self):
        self.speed=self.speed+5
        return self.speed
        
    def stop(self):
        self.speed=0
        return self.speed
        
        
    def info(self):
        return "Information:Make:",self.make,"Model:",self.model,"Color:",self.color,"Price:",self.price

my_car=Car('AUDI','Q8','RED',700000)
initialspeed=my_car.start()
print("Initial speed:",initialspeed)
my_car.info()
my_car.start()
speed=my_car.move()
my_car.move()
print("Speed :",speed)
my_car.stop()
        
    