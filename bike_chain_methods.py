import random
class bike(object):
  def __init__(self, price=None, max_speed=None):
    print 'New Bike!'
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def displayInfo(self):
    print("Price - " + str(self.price) + " USD")
    print("Max Speed - " + str(self.max_speed) + " MPH")
    print("Miles - " + str(self.miles))
    return self
  def ride(self):
    print("Riding...")
    self.miles += 10
    return self
  def reverse(self):
    print("Reversing...")
    if (self.miles < 5):
      self.miles = 0
    else:
      self.miles -= 5
    return self

Huffy = bike(100,15)
Huffy.ride().ride().ride().reverse().displayInfo()

Schwinn = bike(300,20)
Schwinn.ride().ride().reverse().reverse().displayInfo()

Dyno = bike(200,15)
Dyno.reverse().reverse().reverse().displayInfo()
