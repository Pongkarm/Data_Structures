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

class Vehicle:
    def __init__(self, brand, speed, mileage):
        self.brand = brand
        self.speed = speed
        self.mileage = mileage
    
    def reset(self):
        self.mileage = 0
    def where(self):
        print(f'Now mileage is {self.mileage}')
    def move(self, time):
        pass