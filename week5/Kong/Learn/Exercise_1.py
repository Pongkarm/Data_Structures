class Vehicle:
    def __init__(self, brand = '', speed = 0, mileage = 0):
        self.brand = brand
        self.speed = speed
        self.mileage = mileage
        
    def reset(self):
        self.mileage = 0
    
    def where(self):
        print(f'Current distance = {self.mileage} km')
        
    def move(self,time):
        self.mileage += time * self.speed
        
class Bus(Vehicle):
    def __init__(self, brand = '', speed = 0, mileage = 0, bus_number = '', seating_capacity = 0):
        super().__init__(brand, speed, mileage)
        self.bus_number = bus_number
        self.seating_capacity = seating_capacity
        
    def fare(self,money):
        Total_fare = self.mileage * money
        print(f'Total fare = {Total_fare} baht')
        
        
# Exercise_1 Step_1
Car = Vehicle('BMW')
Car.speed = 10
Car.move(5)
Car.where()
Car.reset()
Car.where()
Car.speed = 5
Car.move(8)
Car.where()

# Exercise_1 Step_2
Bus_0 = Bus('Kong')
Bus_0.bus_number = 'A01X'
Bus_0.seating_capacity = 15
Bus_0.speed = 30
Bus_0.move(2)
print(Bus_0.bus_number)
Bus_0.where()

# Exercise_1 Step_3
Bus_1 = Bus('Benz')
Bus_2 = Bus('Benz')
Bus_1.speed = 30
Bus_1.move(2)
Bus_1.where()
Bus_1.fare(5)
Bus_2.speed = 10
Bus_2.move(5)
Bus_2.where()
Bus_2.fare(7)


