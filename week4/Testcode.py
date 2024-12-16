# a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

# def Bubble_sort(a_list):
#     n = len(a_list)
#     while True:    
#         if a_list[j] > a_list[j+1] :
#             a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
#             flag = 1
#     return a_list

# print(a)
# print(Bubble_sort(a))

def factorial_recursive(n):
    if n == 0 or n == 1:  # กรณีฐาน (base case)
        return 1
    else:
        return n * factorial_recursive(n - 1)  # เรียกฟังก์ชันซ้ำโดยลด n ลง 1

# ตัวอย่างการเรียกใช้
print(factorial_recursive(5))  # ผลลัพธ์: 120
