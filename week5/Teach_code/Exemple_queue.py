from Queue import Queue

# สร้างคิวใหม่
queue = Queue()

# เพิ่มข้อมูลลงในคิว
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# ดูจำนวนข้อมูลในคิว
print(len(queue))  # Output: 3

# ดึงข้อมูลออกจากคิว
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20

# ตรวจสอบว่าคิวว่างหรือไม่
print(queue.isEmpty())  # Output: False

# ดึงข้อมูลที่เหลือออก
print(queue.dequeue())  # Output: 30

# ตรวจสอบว่าคิวว่าง
print(queue.isEmpty())  # Output: True

# ลอง dequeue จากคิวว่าง (จะเกิด AssertionError)
# print(queue.dequeue())  # Output: AssertionError

# form chat GPT