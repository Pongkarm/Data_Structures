# Exercise 2
# สร้างโปรแกรม Matching Parentheses โดยใช้ Stack
#  สร้าง Function สำหรับรับค่าตัวอักษร เช่น (5 + 3) x {(30 – 2) + 7}
#  ทำการตรวจสอบว่า ผู้ใช้งานมีการใส่เครื่องหมาย ( ), { } ถูกต้องหรือไม่
#  ถ้าครบคู่ ถูกต้อง ให้พิมพ์คำว่า Correct Format
#  ถ้าไม่ครบคู่ไม่ถูกต้องให้พิมพ์คำว่า Incorrect Format

class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, item):
        self._stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self._stack.pop()
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self._stack[-1]
        return None
    
    def isEmpty(self):
        return len(self._stack) == 0

def isMatchingParentheses(expression):
    stack = Stack()
    # สร้าง Mapping ของวงเล็บ
    matching_pairs = {')': '(', '}': '{'}
    
    for char in expression:
        if char in "({":  # ถ้าเจอวงเล็บเปิด
            stack.push(char)
        elif char in ")}":  # ถ้าเจอวงเล็บปิด
            if stack.isEmpty() or stack.pop() != matching_pairs[char]:
                return "Incorrect Format"
    
    # ถ้า Stack ยังมีวงเล็บค้างอยู่ แสดงว่าขาดคู่
    return "Correct Format" if stack.isEmpty() else "Incorrect Format"

# ทดสอบโปรแกรม
expression1 = "(5 + 3) x {(30 - 2) + 7}"  # ถูกต้อง
expression2 = "(5 + 3) x {30 - 2) + 7}"   # ไม่ถูกต้อง

print(isMatchingParentheses(expression1))  # Output: Correct Format
print(isMatchingParentheses(expression2))  # Output: Incorrect Format

#form chat GPT