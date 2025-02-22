# การหาค่ามากที่สุดใน List ที่ซ้อนกัน (Nested List)
# Recursion ช่วยให้เราสามารถหาค่าที่ใหญ่ที่สุดในโครงสร้างข้อมูลแบบซ้อนกัน
# find_max() ทำอะไร?
# มันคือฟังก์ชันที่ หาค่ามากที่สุด จาก List ที่มีการซ้อนกันหลายชั้น
def find_max(lst):
    if not lst:  # ถ้าเป็น list ว่าง return ค่าน้อยที่สุด
        return float('-inf')
    
    first, rest = lst[0], lst[1:]
    
    if isinstance(first, list):  # ถ้าเป็น list ให้เรียกฟังก์ชันซ้ำ
        first = find_max(first)
    
    return max(first, find_max(rest))

# ตัวอย่างใช้งาน
nested_list = [3, [5, 9], [2, [8, 4]], 6]
print(f"ค่ามากที่สุดคือ {find_max(nested_list)}")


# เริ่มต้นที่ find_max([3, [5, 9], [2, [8, 4]], 6])

# first = 3, rest = [[5, 9], [2, [8, 4]], 6]
# first ไม่ใช่ list → ไป max(3, find_max(rest))
# เรียก find_max([[5, 9], [2, [8, 4]], 6])

# first = [5, 9], rest = [[2, [8, 4]], 6]
# first เป็น list → เรียก find_max([5, 9])
# เรียก find_max([5, 9])

# first = 5, rest = [9]
# first ไม่ใช่ list → max(5, find_max([9]))
# เรียก find_max([9])

# first = 9, rest = []
# first ไม่ใช่ list → max(9, find_max([]))
# find_max([]) → float('-inf')
# max(9, -inf) = 9
# find_max([5, 9]) = max(5, 9) = 9
# กลับไปที่ find_max([[5, 9], [2, [8, 4]], 6])

# first = 9
# max(9, find_max([[2, [8, 4]], 6]))
# เรียก find_max([[2, [8, 4]], 6])

# first = [2, [8, 4]]
# first เป็น list → เรียก find_max([2, [8, 4]])
# เรียก find_max([2, [8, 4]])

# first = 2, rest = [[8, 4]]
# first ไม่ใช่ list → max(2, find_max([[8, 4]]))
# เรียก find_max([[8, 4]])

# first = [8, 4]
# first เป็น list → find_max([8, 4])
# เรียก find_max([8, 4])

# first = 8, rest = [4]
# first ไม่ใช่ list → max(8, find_max([4]))
# เรียก find_max([4])

# first = 4, rest = []
# max(4, find_max([])) = max(4, -inf) = 4
# find_max([8, 4]) = max(8, 4) = 8
# ย้อนกลับไป find_max([2, [8, 4]])

# max(2, 8) = 8
# ย้อนกลับไป find_max([[2, [8, 4]], 6])

# max(8, find_max([6]))
# เรียก find_max([6])

# first = 6, rest = []
# max(6, find_max([])) = max(6, -inf) = 6
# ย้อนกลับไป find_max([[2, [8, 4]], 6])

# max(8, 6) = 8
# ย้อนกลับไป find_max([[5, 9], [2, [8, 4]], 6])

# max(9, 8) = 9
# ย้อนกลับไป find_max([3, [5, 9], [2, [8, 4]], 6])

# max(3, 9) = 9
# ✅ ค่ามากที่สุดที่หาได้คือ 9