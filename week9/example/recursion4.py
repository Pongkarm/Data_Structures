# การหาค่ามากที่สุดใน List ที่ซ้อนกัน (Nested List)
# Recursion ช่วยให้เราสามารถหาค่าที่ใหญ่ที่สุดในโครงสร้างข้อมูลแบบซ้อนกัน
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
