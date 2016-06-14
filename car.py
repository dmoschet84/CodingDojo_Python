import random
class Car(object):
    def __init__(self, price=None, speed=None, fuel=None, mileage=None):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed) + "mph")
        print("Fuel: " + self.fuel)
        print("Mileage: " + str(self.mileage) + "mpg")
        print("Tax: " + str(self.tax))
        print("")
Ford = Car(2000,35,"Full",15)
Chevy = Car(15000,50,"Not Full",105)
Pontiac = Car(5000,15,"Kind of Full",95)
Toyota = Car(2000,75,"Full",55)
Honda = Car(11000,65,"Half Full",80)
