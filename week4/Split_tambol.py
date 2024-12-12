#this file is split file tambol to txt
import re
def read_sql_file_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r"\((\d+), '([^']+)', (\d+), '([^']+)', (\d+), '([^']+)'\)"  # ใช้ \w+ เพื่อจับตัวอักษรและตัวเลขของ code

    matches = re.findall(pattern, content)
    return matches

# รายชื่อไฟล์ที่ต้องการประมวลผล
files = [
    "tambol.sql"
]

for file_path in files:
    data = read_sql_file_and_process(file_path)
    print(f"Processed data from {file_path}:")
    for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
        print(row)
    print("\n")
    
with open('tambol.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}\n")