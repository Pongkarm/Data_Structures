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


def check_parentheses(expression):
    stack = Stack()
    # Dictionary to map closing to opening parentheses
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "({[":
            stack.push(char)  # Push opening parentheses to the stack
        elif char in ")}]":
            if stack.isEmpty():
                print("Incorrect Format")
                return
            top = stack.pop()
            if matching[char] != top:
                print("Incorrect Format")
                return

    # If the stack is empty after processing the expression, it's correct
    if stack.isEmpty():
        print("Correct Format")
    else:
        print("Incorrect Format")

if __name__ == "__main__":
    print("\n\n")
    check_parentheses("{3+[(6-2)]}")
    print("\n\n")

#form Teacher

# class Stack:

#     def __init__(self):
#         self._top = None
#         self._size = 0

#     def isEmpty(self):
#         return self._top is None
    
#     def __len__(self):
#         return self._size
    
#     def peek(self):
#         assert not self.isEmpty(), "Cannot peek at an empty stack"
#         return self._top.item

#     def pop(self):
#         assert not self.isEmpty(), "Cannot pop from an empty stack"
#         node = self._top
#         self._top = self._top.next
#         self._size = self._size - 1
#         return node.item

#     def push(self, item):
#         self._top = _StackNode(item, self._top)
#         self._size = self._size + 1

# class _StackNode:
#     def __init__(self, item, link):
#         self.item = item
#         self.next = link
        
# # Exercise_2
# def Matching_Parentheses(message):
#     stack = Stack()
#     opening_parentheses = ['(', '[', '{']
#     closing_parentheses = [')', ']', '}']

#     for char in message:
        
#         # ถ้าตัวอักษร char เป็นเครื่องหมายวงเล็บเปิด ((, [, {):
#         # ใช้เมธอด push ของ Stack เพื่อเพิ่มเครื่องหมายวงเล็บนี้เข้าไปในสแต็ก
#         if char in opening_parentheses: 
#             stack.push(char)
            
#         # ถ้าตัวอักษร char เป็นเครื่องหมายวงเล็บปิด (), ], }):
# 		# ตรวจสอบว่าสแต็กว่างหรือไม่ (ไม่มีเครื่องหมายวงเล็บเปิดที่ตรงกัน):
# 		# ถ้าสแต็กว่าง (stack.isEmpty() คืนค่า True): แสดงว่าข้อความผิดรูปแบบ เพราะมีเครื่องหมายวงเล็บปิดโดยไม่มีเครื่องหมายวงเล็บเปิดที่ตรงกัน → คืนค่า "Incorrect Format"
#         elif char in closing_parentheses:
#             if stack.isEmpty():
#                 return "Incorrect Format"
            
# 			# ใช้เมธอด pop ของ Stack เพื่อนำเครื่องหมายวงเล็บเปิดด้านบนสุดของสแต็กออกมา (เก็บไว้ในตัวแปร top_opening_parenthesis)
# 			# ตรวจสอบว่าประเภทของเครื่องหมายวงเล็บเปิด (top_opening_parenthesis) ตรงกับเครื่องหมายวงเล็บปิด (char) หรือไม่ โดยใช้ฟังก์ชัน index:
# 			# opening_parentheses.index(top_opening_parenthesis): หาตำแหน่งของเครื่องหมายวงเล็บเปิด
# 			# closing_parentheses.index(char): หาตำแหน่งของเครื่องหมายวงเล็บปิด
# 			# ถ้าตำแหน่งไม่ตรงกัน → คืนค่า "Incorrect Format"
#             top_opening_parenthesis = stack.pop()
#             if opening_parentheses.index(top_opening_parenthesis) != closing_parentheses.index(char):
#                 return "Incorrect Format"
            
# 	# หลังจากวนลูปตรวจสอบครบทุกตัวอักษรแล้ว:
# 	# ถ้าสแต็กว่าง (stack.isEmpty() คืนค่า True): แสดงว่าเครื่องหมายวงเล็บทั้งหมดจับคู่กันเรียบร้อย → คืนค่า "Correct Format"
# 	# ถ้าสแต็กไม่ว่าง: แสดงว่ายังมีเครื่องหมายวงเล็บเปิดที่ไม่มีคู่ → คืนค่า "Incorrect Format"
#     if stack.isEmpty():
#         return "Correct Format"
#     else:
#         return "Incorrect Format"

# # Ex
# print(Matching_Parentheses('(5 + 3) x {(30 - 2) + 7}'))  # Correct Format
# print(Matching_Parentheses('(5 + 3) x {(30 - 2) + 7'))   # Incorrect Format
# By Kong
