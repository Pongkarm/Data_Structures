import timeit
start_time = timeit.default_timer()
#this file is split file amphoe to txt
import re
def read_sql_file_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r"\((\w+), '([^']+)', (\w+), '([^']+)'\)"  # ใช้ \w+ เพื่อจับตัวอักษรและตัวเลขของ code
    matches = re.findall(pattern, content)
    return matches

# รายชื่อไฟล์ที่ต้องการประมวลผล
files = [
    "week4/amphoe.sql"
]

for file_path in files:
    data = read_sql_file_and_process(file_path)
    print(f"Processed data from {file_path}:")
    for row in data[:5]:  # แสดงข้อมูล 5 บรรทัดแรกเพื่อดูตัวอย่าง
        print(row[0], row[3])
    print("\n")
    
with open('week4/amphoe.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[3]}\n")

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")