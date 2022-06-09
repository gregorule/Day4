class Vehicle:

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}"
    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)
    def fare(self):
        amount = super().fare()
        new_amount = amount * 1.1
        return new_amount

class Car(Vehicle):
    pass


bus1 = Bus("School bus", 25, 3456789, 50)
print(bus1.mileage)
print(bus1.__dict__)

print(bus1.fare())
