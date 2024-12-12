#แบบแรก หาจังหวัดผ่านเลข จากfile result_province.txt
import re

# # รับ input จากผู้ใช้
# user = input('ใส่จังหวัดที่ต้องการหา เช่น "กรุงเทพมหานคร" หรือ "10": ')

# # เปิดไฟล์และค้นหาข้อมูล
# with open('result_province.txt', 'r', encoding='utf-8') as file:
#  for line in file:
#         if re.search(re.escape(user), line):
#             # ดึงข้อมูลในวงเล็บ
#             match = re.search(r"\('(\d+)', '([^']+)'\)", line)
#             if match:
#                 province_code = match.group(1)  # รหัสจังหวัด
#                 province_name = match.group(2)  # ชื่อจังหวัด
#                 print(f"{province_code}, {province_name}")


#แบบสอง หาจังหวัดผ่านเลข จากfile amphoe.sql

# รับ input จากผู้ใช้
user = input('ใส่จังหวัดที่ต้องการหา เช่น "กรุงเทพมหานคร" หรือ "เลขรหัส": ')

# เปิดไฟล์และค้นหาข้อมูล
with open('amphoe.txt', 'r', encoding='utf-8') as file:
 for line in file:
    if re.search(re.escape(user), line):
        match = re.search(r"'(\d{4})'\s'([ก-์a-zA-Z0-9]+)'\s'(\d{2})'\s'([ก-์a-zA-Z0-9]+)'", line)
        print(line)
        # if match:
        #     code_group = match.group(1)  # รหัสกลุ่ม (0313)
        #     group_name = match.group(2)  # ชื่อกลุ่ม (กลุ่มตรวจสอบภายใน)
        #     code_department = match.group(3)  # รหัสหน่วยงาน (03)
        #     department_name = match.group(4)  # ชื่อหน่วยงาน (กรมการปกครอง)
        #     print(f'รหัสกลุ่ม {code_group}')
        #     print(f'ชื่อกลุ่ม {group_name}')
        #     print(f'รหัสหน่วยงาน {code_department}')
        #     print(f'ชื่อหน่วยงาน {department_name}')
        # else:
        #     print('no found ')
        #     print(line)
        
    #แม่งใส่ หลักสองตัวม่ได้จะไปซ้ำกับตัวแรก ปล่องแม่งเป็นงี้แหละ