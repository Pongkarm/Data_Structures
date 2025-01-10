import timeit
start_time = timeit.default_timer()

def Insertion_sort(a_list):
    n = len(a_list)
    for i in range(1, n):
        temp = a_list[i]
        hole = i
        while hole > 0 and a_list[hole - 1] > temp:
            a_list[hole] = a_list[hole - 1]
            hole -= 1
        a_list[hole] = temp
    return a_list

a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

print("Original list:", a)
print("Sorted list:", Insertion_sort(a))


elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")


#ถ้าอ่านไม่เข้าใจให้อ่านโค้ดไปด้วยพร้อมใช้สมองอันน้อยนิดคิดตาม555 ล้อเล่นนะครับคนทำยังอ่านตั้งหลายรอบเลยกว่าจะเข้าใจ love love na
#เริ่มอธิบายตั้งแต่ line 6
a = [4, 7, 9, 2]
# รอบที่ 1
# i = 1-------
# temp = 7   | same
#hole = 1-----
# 4 > 7 ?  NO ไม่ทำใน whileloop (line 9)
#a_list[hole] = temp  7 แทน 7 ใน a

# รอบที่ 2
# i = 2------
# temp = 9  | same
#hole = 2----
# 7 > 9 ?  NO ไม่ทำใน whileloop (line 9)
#a_list[hole] = temp  9 แทน 9 ใน a

# รอบที่ 2
# i = 3------
# temp = 2  | same
#hole = 3----
# 9 > 2 ?  yes ทำใน whileloop (line 9)
#สลับเอา 9 มาไว้แทน 2  [4, 7, 9, 2] >> a = [4, 7, 9, 9] (line 10)
#hole = 3 - 1 (line 11)
#กลับไปเช็ค loop  7 > 2 ? yes ทำใน whileloop (line 9)
#สลับเอา 7 มาไว้ที่ hole(2)  [4, 7, 9, 9] >> a = [4, 7, 7, 9] (line 10)
#hole = 2 - 1
#กลับไปเช็ค loop  4 > 2 ? yes ทำใน whileloop (line 9)
#a_list[hole] = temp  4 แทน 7 [4, 7, 9, 9] >> a = [4, 4, 7, 9]
#hole = 1-1
#เมื่อกลับไปเช็คใน while loop ไม่มากกว่า 0 หรือ เลข temp(2)ไม่น้อยกว่า list (a_[hole - 1]) ก็จบloop
#ทำให้ a[hole] (ในที่นี้hole=0) = temp(2) [4, 4, 7, 9] >> [2, 4, 7, 9] (line12)

#จบ for loop 