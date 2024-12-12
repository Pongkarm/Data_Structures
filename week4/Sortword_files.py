# import re
# #เราจะใช้ความรู้อันน้อยนิดของเราทำดู
# with open('province.sql', 'r', encoding='utf-8') as province:
#   for line in province:
#     x = line.split()
#     x = x[7:9]
#     x = x
#     print(x)


import re
# 111111111111111111111111
# ฟังก์ชันสำหรับอ่านไฟล์และแยกข้อมูลเฉพาะ code กับ name
# def read_sql_file_and_process(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()

#     # ใช้ regex เพื่อจับข้อมูลทุกชุดที่มีรูปแบบ (code, name, ...), รองรับหลายชื่อ
#     # เช่น acode, fcode, aname, fname หรือชื่ออื่น ๆ ที่อาจมี
#     pattern = r"\((\w+),\s*'([^']+)',"  # ใช้ \w+ เพื่อจับตัวอักษรและตัวเลขของ code
#     matches = re.findall(pattern, content)

#     return matches

# # รายชื่อไฟล์ที่ต้องการประมวลผล
# files = [
#     "province.sql"
# ]

# # อ่านและประมวลผลแต่ละไฟล์
# for file_path in files:
#     data = read_sql_file_and_process(file_path)
#     print(f"Processed data from {file_path}:")
#     for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
#         print(row)
#     print("\n")
    
# with open('result_province.txt', 'w', encoding='utf-8') as write_province:
#   for row in data:
#     write_province.write(f"('{row[0]}', '{row[1]}'),\n")


# 22222222222222222222222222222 
# amphoe.sql
# def read_sql_file_and_process(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#     pattern = r"\((\w+), '([^']+)', (\w+), '([^']+)'\)"  # ใช้ \w+ เพื่อจับตัวอักษรและตัวเลขของ code
#     matches = re.findall(pattern, content)
#     return matches

# # รายชื่อไฟล์ที่ต้องการประมวลผล
# files = [
#     "amphoe.sql"
# ]

# อ่านและประมวลผลแต่ละไฟล์
# for file_path in files:
#     data = read_sql_file_and_process(file_path)
#     print(f"Processed data from {file_path}:")
#     for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
#         print(row)
#     print("\n")
    
# with open('amphoe.txt', 'w', encoding='utf-8') as write_province:
#   for row in data:
#     write_province.write(f"'{row[0]}' '{row[1]}' '{row[2]}' '{row[3]}'\n")
# #3333333333333333333333333333
# def read_sql_file_and_process(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#     pattern = r"\((\d+), '([^']+)', (\d+), '([^']+)', (\d+), '([^']+)'\)"  # ใช้ \w+ เพื่อจับตัวอักษรและตัวเลขของ code

#     matches = re.findall(pattern, content)
#     return matches

# # รายชื่อไฟล์ที่ต้องการประมวลผล
# files = [
#     "tambol.sql"
# ]

# for file_path in files:
#     data = read_sql_file_and_process(file_path)
#     print(f"Processed data from {file_path}:")
#     for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
#         print(row)
#     print("\n")
    
# with open('tambol.txt', 'w', encoding='utf-8') as write_province:
#   for row in data:
#     write_province.write(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}\n")
# 444444444444444444444444444444444444444

def read_sql_file_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r"\('([^']+)', '([^']+)', (\d+), (\d+), (\d+), '([^']+)', (\d+), '([^']+)', (\d+), '([^']+)', '([^']+)', '([^']+)', '([^']+)', (NULL|'[^']+'), '([^']+)', (NULL|\d+), (NULL|\d+), (NULL|\d+)\)"
          
    matches = re.findall(pattern, content)
    return matches

# รายชื่อไฟล์ที่ต้องการประมวลผล
files = [
    "mm.sql"
]

for file_path in files:
    data = read_sql_file_and_process(file_path)
    print(f"Processed data from {file_path}:")
    for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
        print(row)
    print("\n")
    
with open('mm.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]} {row[11]} {row[12]} {row[13]} {row[14]} {row[15]} {row[16]} {row[17]}\n")