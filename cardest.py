#!/usr/bin/python3

class Car(object):
    avg_mph = 60.0
    capacity = 100.0
    fuel_capacity = 10
    fuel = 5
    mpg = 100
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def eta(self, distance):
        print(distance, self.avg_mph)
        print(self.fuel_check(distance))
        return 'Arrive in %sy style in %s hours' % (self.colour, str(distance / self.avg_mph))

    def luggage_check(self, luggage):
        if luggage < self.capacity:
            return "The luggage will fit in your %s and there will be %s spare capacity" % (self.model, str(self.capacity - luggage))
        elif luggage == self.capacity:
            return "The luggage will fit exactly in your %s so there will be no spare capacity" % self.model
        else:
            return "The luggage will not fit in your %s unless you remove %s of luggage first" % (self.model, str(luggage - self.capacity))

    def fuel_check(self, distance):
        if distance > self.mpg * self.fuel:
            return 'You do not have enough fuel for this journey'
        else:
            return 'You have enough fuel for this journey'

        # return 'You will need to fill up %s times on the journey' % 



class Toyota(Car):
    avg_mph = 40.0
    capacity = 40.0
    fuel_capacity = 8.0
    mpg = 70
    fuel = 5.0

class Ford(Car):
    avg_mph = 50.0
    capacity = 60.0
    fuel_capacity = 9.0
    mpg = 50
    fuel = 7.0

class Ferrari(Car):
    avg_mph = 120.0
    capacity = 20.0
    fuel_capacity = 13.0
    mpg = 20
    fuel = 7.0

# todo
# user choice of car
# user entry of distance

my_car  = Toyota('Toyota', 'pink')
your_car  = Ford('Ford', 'purple')
her_car  = Ferrari('Ferrari', 'orange')

print(my_car.eta(500))
print(your_car.eta(350))
print(her_car.eta(265))

print(my_car.luggage_check(55))
print(your_car.luggage_check(55))
print(her_car.luggage_check(55))


