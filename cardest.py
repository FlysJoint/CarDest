#!/usr/bin/python3

class Car(object):
    avg_speed = 60.0
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def eta(self, distance):
        return 'Arrive in %sy style in %s hours' % (self.colour, str(distance / self.avg_speed))

class Toyota(Car):
    avg_speed = 40.0

class Ford(Car):
    avg_speed = 50.0

# todo
# user choice of car
# user entry of distance

my_car  = Toyota('Toyota', 'Pink')
your_car  = Ford('Ford', 'Purple')

print(my_car.eta(100))
print(your_car.eta(100))


