import os

def list_files(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(f"[Folder] {path}")
            list_files(path)  # เรียกฟังก์ชันตัวเองเพื่อค้นหาในโฟลเดอร์ย่อย
        else:
            print(f"[File] {path}")

# ตัวอย่างใช้งาน
list_files("C:/Users/YourUsername/Documents")