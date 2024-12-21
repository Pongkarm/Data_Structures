from week5.Teach_code.Stack import Stack 

stack = Stack()

# เพิ่มข้อมูลใน Stack
stack.push(10)
stack.push(20)
stack.push(30)

# ดูค่าด้านบนสุด
print(stack.peek())  # Output: 30

# ลบข้อมูลด้านบนสุด
print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20

# เช็คขนาดของ Stack
print(len(stack))    # Output: 1

# เช็คว่า Stack ว่างไหม
print(stack.isEmpty())  # Output: False
