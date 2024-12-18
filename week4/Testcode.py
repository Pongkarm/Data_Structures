def factorial_recursive(n):
    if n == 0 or n == 1:  # กรณีฐาน (base case)
        return 1
    else:
        return n * factorial_recursive(n - 1)  # เรียกฟังก์ชันซ้ำโดยลด n ลง 1

# ตัวอย่างการเรียกใช้
print(factorial_recursive(5))

def pongkarm(n):
    if n == 0:
        return n 
    else:
        return n + pongkarm(n - 1)

print(pongkarm(9))
    