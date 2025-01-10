import timeit
start_time = timeit.default_timer()
a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

def Bubble_sort(a_list):
    n = len(a_list)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            #swap
            if a_list[j] > a_list[j+1] :
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                flag = 1
        if flag == 0:
            break
    return a_list

print(a)
print(Bubble_sort(a))

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")

#เริ่มอธิบาย line 7
a = [4, 9, 7, 2]

# รอบแรกของ for i 
#  i = 0
#  for j จะวนจำนวน n-i-1 (เมื่อ j ถึง 3 ก็จะจบ) เราจะใช้ j เป็นตัวเรียกค่าใน a lise
# j = 0 
#ตรวจว่า a[j] > a[j+1] แปลงให้เข้าใจขึ้นเป็น a[0] > a[0+1] (line 11)
# จะหมายความว่า 4 > 9 ?? ไม่เป็นจริง 
#จะจบ loop j 1ครั้ง  j = j+1 (line 9)
#j = 1
#ตรวจว่า a[j] > a[j+1] ซึ่งหมายความว่า 9 > 7 ?? เป็นจริง  (line 10)
#จะทำการสลับตำแหน่ง a[j],[j+1] = a[j+1], a[j] (line12)
#ใน list a จะเปลี่ยนจาก [4, 9, 7, 2] >> a = [4, 7, 9, 2]
#จบ loop  j+1
#j = 2
#ครวจเหมือนดิม a[2] > a[2+1] (line 11)
# 7 > 2 ?? เป็นจริง
#จะทำการสลับตำแหน่ง a[j],[j+1] = a[j+1], a[j] (line12)
#ใน list a จะเปลี่ยนจาก [4, 9, 7, 2] >> a = [4, 7, 2, 9]
#j + 1  >> j = 3 จบloop j

#ได้ a = [4, 7, 2, 9]
# รอบ 2 ของ for i 
#  i = 1
#  for j จะวนจำนวน n-i-1 (เมื่อ j ถึง 2 ก็จะจบ) loop j เราก็จะวนน้อยลงไป
# j = 0
# ตรวจว่า a[j] > a[j+1] จะหมายความว่า 4 > 7 ?? ไม่เป็นจริง 
#จะจบ loop j 1ครั้ง  j = j+1 (line 9)
#j = 1
# ตรวจว่า a[j] > a[j+1] จะหมายความว่า 7 > 2 ?? เป็นจริง 
#จะทำการสลับตำแหน่ง a[j],[j+1] = a[j+1], a[j] (line12)
#ใน list a จะเปลี่ยนจาก #ได้ a = [4, 7, 2, 9] >> [4, 2, 7, 9]
#j += 1
#และจบ loop j  เพราะ j เท่ากับ 2 แล้วตามเงื่อนไข (line 9)

#ทำไปเรื่อยๆจนจบ loop i ก็จะเสร็จ