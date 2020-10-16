#!/usr/bin/python3

class Car(object):
    avg_speed = 60.0
    capacity = 100.0
    fuel_capacity = 10
    fuel = 5
    mpg = 100
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def eta(self, distance):
        print(self.fuel_check(distance))
        return 'Arrive in %sy style in %s hours' % (self.colour, str(distance / self.avg_speed))

    def luggage_check(self, luggage):
        if luggage < self.capacity:
            return "The luggage will fit and there will be %s spare capacity" % str(self.capacity - luggage)
        elif luggage == self.capacity:
            return "The luggage will fit exactly so there will be no spare capacity"
        else:
            return "The luggage will not fit unless you remove %s of luggage first" % str(luggage - self.capacity)

    def fuel_check(self, distance):
        if distance > self.mpg * self.fuel:
            return 'You do not have enough fuel for this journey'
        else:
            return 'You have enough fuel for this journey'

        # return 'You will need to fill up %s times on the journey' % 



class Toyota(Car):
    avg_speed = 40.0
    capacity = 40.0
    fuel_capacity = 8.0
    mpg = 70
    fuel = 5.0

class Ford(Car):
    avg_speed = 50.0
    capacity = 60.0
    fuel_capacity = 9.0
    mpg = 50
    fuel = 7.0

# todo
# user choice of car
# user entry of distance

my_car  = Toyota('Toyota', 'Pink')
your_car  = Ford('Ford', 'Purple')

print(my_car.eta(500))
print(your_car.eta(350))

print(my_car.luggage_check(55))
print(your_car.luggage_check(55))


