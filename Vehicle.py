

class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def toString(self):
        return f"This vehicle is {self.color}"



class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires
    
    def toString(self):
        return f"{super().toString()}\nHas winter tires: {self.has_winter_tires}"



class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer
    
    def toString(self):
        return f"{super().toString()}\nHas trailer: {self.has_trailer}"


class Garage:
    def __init__(self):
        self.vehicle = None
    
    def setVehicle(self, parked):
        self.vehicle = parked
    
    def toString(self):
        if self.vehicle:
            return f"Description of the parked vehicle:\n{self.vehicle.toString()}"
        else:
            return "No vehicle is parked in the garage."
        

class GarageTester:
    def getExample(self):
        truck = Truck("black", has_trailer=False)
        garage = Garage()
        garage.setVehicle(truck)
        print(garage.toString())

# To test the functionality
tester = GarageTester()
tester.getExample()

#if I comment the customer class out and run the code, it gives the required output
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer Name: {self.name}\nAddress: {self.address}"

