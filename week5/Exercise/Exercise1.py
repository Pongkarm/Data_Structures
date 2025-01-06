# Exercise #1
# สร้าง Object ชื่อ Car
# กำหนดให้ความเร็วของ Car (speed) เท่ากับ 10
# ทดลองใช้ Function move กำหนดว่า time = 5
# แสดงระยะทางสะสมที่ Car เคลื่อนที่ไปได้

#step2
# เขียน Class รถประจำทาง (Bus) ที่สืบทอด (inherit) มาจาก Vehicle โดยให้เพิ่ม Attribute เกี่ยวกับ
# หมายเลขรถ (bus_number)
# จำนวนที่นั่ง (seating_capacity)
# กำหนดหมายเลขรถ และจำนวนที่นั่ง (A01X, 15 ที่นั่ง)
# สั่งให้เคลื่อนที่ไปด้วยความเร็ว 30 km/hr. เป็นระยะเวลา 2 hrs.
# สั่ง print กำหนดหมายเลขรถและระยะทางสะสม

# step3
# เพิ่มอัตราค่าโดยสารตามระยะทาง (fare_rate) และเขียน Function ในการคำนวณค่าโดยสารใน Bus
# สร้าง Object รถ Bus ขึ้นมา 2 คัน
# คันที่ 1: Mercedes-Benz เคลื่อนที่ด้วยความเร็ว 30km/hr. ระยะเวลา 2 hrs. และมีอัตราค่าโดยสาร 1 km / 5 บาท
# คันที่ 2: Volvo เคลื่อนที่ด้วยความเร็ว 10km/hr. ระยะเวลา 5 hrs. และมีอัตราค่าโดยสาร 1 km / 7 บาท
# สั่งคำนวณและแสดงค่าโดยสารรวมที่เกิดขึ้นและระยะทางสะสมของรถทั้ง 2 คัน

# step 1
class Vehicle:
    def __init__(self, brand='', speed=0, mileage=0):
        self.brand = brand
        self.speed = speed
        self.mileage = mileage
    
    def reset(self):
        self.mileage = 0
    def where(self):
        print(f'Now mileage is {self.mileage}')
    def move(self, time):
        self.mileage += time * self.speed

# step2
class Bus(Vehicle):
    def __init__(self, brand='', speed=0, mileage=0, bus_number= '', seating_capacity=0):
        super().__init__(brand, speed, mileage)
        self.bus_number = bus_number
        self.seating_capacity = seating_capacity

# step3
def fare(mileage, money):
    return mileage * money



# step1
# if __name__ == '__main__':        
#     car1 = Vehicle('Kond')
#     car1.speed = 5 
#     car1.where()
#     car1.move(2)
#     car1.where()
#     car1.move(6)
#     car1.where()
#     car1.reset()
#     car1.where()


# step2
# if __name__ == '__main__':        
#     car1 = Bus('Pongkarm')
#     car1.speed = 30
#     car1.bus_number = 'A01X'
#     car1.seating_capacity = 15
#     car1.where()
#     car1.move(2)
#     print(car1.bus_number)
#     car1.where()

# step3
if __name__ == '__main__':        
    car1 = Bus('Pongkarm')
    car1.speed = 30
    car1.bus_number = 'A01X'
    car1.seating_capacity = 15
    car1.where()
    car1.move(2)
    print(fare(car1.mileage, 5))
    car2 = Bus('Kong')
    car2.speed = 10
    car2.bus_number = 'A02X'
    car2.move(5)
    print(fare(car2.mileage, 7))
#by Pongkarm

# class Vehicle:
#     def __init__(self, brand = '', speed = 0, mileage = 0):
#         self.brand = brand
#         self.speed = speed
#         self.mileage = mileage
        
#     def reset(self):
#         self.mileage = 0
    
#     def where(self):
#         print(f'Current distance = {self.mileage} km')
        
#     def move(self,time):
#         self.mileage += time * self.speed
        
# class Bus(Vehicle):
#     def __init__(self, brand = '', speed = 0, mileage = 0, bus_number = '', seating_capacity = 0):
#         super().__init__(brand, speed, mileage)
#         self.bus_number = bus_number
#         self.seating_capacity = seating_capacity
        
#     def fare(self,money):
#         Total_fare = self.mileage * money
#         print(f'Total fare = {Total_fare} baht')
        
        
# # Exercise_1 Step_1
# Car = Vehicle('BMW')
# Car.speed = 10
# Car.move(5)
# Car.where()
# Car.reset()
# Car.where()
# Car.speed = 5
# Car.move(8)
# Car.where()

# # Exercise_1 Step_2
# Bus_0 = Bus('Kong')
# Bus_0.bus_number = 'A01X'
# Bus_0.seating_capacity = 15
# Bus_0.speed = 30
# Bus_0.move(2)
# print(Bus_0.bus_number)
# Bus_0.where()

# # Exercise_1 Step_3
# Bus_1 = Bus('Benz')
# Bus_2 = Bus('Benz')
# Bus_1.speed = 30
# Bus_1.move(2)
# Bus_1.where()
# Bus_1.fare(5)
# Bus_2.speed = 10
# Bus_2.move(5)
# Bus_2.where()
# Bus_2.fare(7)
# By Kong