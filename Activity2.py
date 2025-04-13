class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

vehicle1 = Car()
vehicle2 = Plane()

vehicle1.move()  
vehicle2.move()  
