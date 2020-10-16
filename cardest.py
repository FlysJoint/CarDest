#!/usr/bin/python3

class Car(object):
    avg_speed = 60.0
    def __init__(self, make):
      self.make = make

    def eta(self, distance):
        return distance / self.avg_speed

my_car  = Car('Aygo')

print(my_car.eta(100))


